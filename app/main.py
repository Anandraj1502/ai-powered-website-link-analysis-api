from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.services.analysis_service import analyze_website
from app.utils.validators import validate_url
from app.schemas import LinkAnalysisResponse


app = FastAPI(
    title="AI-Powered Website Link Analysis API",
    description="Analyze websites using AI for business and SEO insights.",
    version="1.0.0",
)


class LinkAnalysisRequest(BaseModel):
    url: str


@app.get("/")
async def home():
    return {
        "message": "AI Website Link Analysis API is running!"
    }


@app.post("/link-analysis", response_model=LinkAnalysisResponse)
async def link_analysis(request: LinkAnalysisRequest):
    try:
        validated_url = validate_url(request.url)

        result = await analyze_website(validated_url)

        return {
            "success": True,
            "data": result,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    except Exception as e:
        print(f"Analysis error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Website analysis failed. Please try again.",
        )