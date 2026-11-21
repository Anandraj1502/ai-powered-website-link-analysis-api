from app.services.website_extractor import extract_website_content
from app.services.llm_service import generate_analysis


async def analyze_website(url: str) -> dict:
    # Step 1: Extract website information
    website_data = await extract_website_content(url)

    # Step 2: Generate AI analysis
    analysis = await generate_analysis(website_data)

    # Step 3: Combine website information and AI analysis
    return {
        "website": website_data,
        "analysis": analysis,
    }