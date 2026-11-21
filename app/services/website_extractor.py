
import httpx
from bs4 import BeautifulSoup
from app.utils.validators import validate_url

MAX_CONTENT_SIZE = 1_000_000  # 1 MB
MAX_REDIRECTS = 5


async def extract_website_content(url: str) -> dict:
    current_url = validate_url(url)

    timeout = httpx.Timeout(15.0)

    async with httpx.AsyncClient(
        timeout=timeout,
        follow_redirects=False,
        headers={"User-Agent": "DxoraLinkAnalysisBot/1.0"},
    ) as client:

        for redirect_count in range(MAX_REDIRECTS + 1):
            current_url = validate_url(current_url)

            async with client.stream("GET", current_url) as response:

                # Handle redirects manually
                if response.is_redirect:
                    if redirect_count >= MAX_REDIRECTS:
                        raise ValueError("Too many redirects.")

                    location = response.headers.get("location")
                    if not location:
                        raise ValueError("Invalid redirect.")

                    current_url = str(
                        httpx.URL(current_url).join(location)
                    )
                    continue

                response.raise_for_status()

                content_type = response.headers.get("content-type", "")
                if "text/html" not in content_type.lower():
                    raise ValueError("URL is not an HTML website.")

                # Download with a size limit
                chunks = []
                total_size = 0

                async for chunk in response.aiter_bytes():
                    total_size += len(chunk)

                    if total_size > MAX_CONTENT_SIZE:
                        raise ValueError("Website content is too large.")

                    chunks.append(chunk)

                html = b"".join(chunks).decode(
                    response.encoding or "utf-8",
                    errors="replace"
                )

                soup = BeautifulSoup(html, "html.parser")

                # Remove unnecessary HTML elements
                for element in soup.select(
                    "script, style, noscript, svg, iframe"
                ):
                    element.decompose()

                # Extract title
                title_tag = soup.find("title")
                title = title_tag.get_text(strip=True) if title_tag else ""

                # Extract meta description
                meta = soup.find("meta", attrs={"name": "description"})
                description = meta.get("content", "") if meta else ""

                # Extract headings
                headings = [
                    tag.get_text(" ", strip=True)
                    for tag in soup.find_all(["h1", "h2", "h3"])
                    if tag.get_text(strip=True)
                ]

                # Extract readable text
                text = soup.get_text(separator=" ", strip=True)
                cleaned_text = " ".join(text.split())[:15000]

                return {
                    "url": str(response.url),
                    "title": title,
                    "description": description,
                    "headings": headings[:40],
                    "content": cleaned_text,
                    "content_length": len(cleaned_text),
                }

    raise ValueError("Unable to extract website content.")
