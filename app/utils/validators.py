
import ipaddress
import socket
from urllib.parse import urlparse


def is_unsafe_ip(ip_string: str) -> bool:
    ip = ipaddress.ip_address(ip_string)

    return (
        ip.is_private
        or ip.is_loopback
        or ip.is_link_local
        or ip.is_reserved
        or ip.is_multicast
        or ip.is_unspecified
    )


def validate_url(url: str) -> str:
    if not url or not isinstance(url, str):
        raise ValueError("URL is required.")

    url = url.strip()

    if len(url) > 2048:
        raise ValueError("URL is too long.")

    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only HTTP and HTTPS URLs are allowed.")

    hostname = parsed.hostname

    if not hostname:
        raise ValueError("Invalid URL: hostname is missing.")

    if parsed.username or parsed.password:
        raise ValueError("URLs containing credentials are not allowed.")

    hostname = hostname.lower().rstrip(".")

    if hostname == "localhost" or hostname.endswith(".localhost"):
        raise ValueError("Localhost URLs are not allowed.")

    # Check if hostname is an IP address
    try:
        ip = ipaddress.ip_address(hostname)

    except ValueError:
        # It is a domain name, so resolve it using DNS
        try:
            results = socket.getaddrinfo(
                hostname,
                None,
                type=socket.SOCK_STREAM,
            )
        except socket.gaierror:
            raise ValueError("Hostname could not be resolved.")

        if not results:
            raise ValueError("Hostname could not be resolved.")

        # Block domain names pointing to unsafe IPs
        for result in results:
            resolved_ip = result[4][0]

            if is_unsafe_ip(resolved_ip):
                raise ValueError(
                    "URL resolves to a private or unsafe IP address."
                )

    else:
        # Direct IP address
        if is_unsafe_ip(str(ip)):
            raise ValueError("Private or unsafe IP addresses are not allowed.")

    return url
