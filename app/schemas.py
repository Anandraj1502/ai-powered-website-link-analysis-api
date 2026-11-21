from pydantic import BaseModel
from typing import List, Optional


class Competitor(BaseModel):
    name: str
    reason: str
    status: str = "AI-inferred"


class SearchQuerySuggestion(BaseModel):
    query: str
    platform: str
    search_intent: str
    business_relevance: str
    target_audience: str


class SEORecommendations(BaseModel):
    recommended_title: str
    meta_description: str
    keywords: List[str]
    content_suggestions: List[str]


class WebsiteAnalysis(BaseModel):
    business_overview: str
    brand_positioning: str
    target_audience: str
    strengths: List[str]
    weaknesses: List[str]
    market_gaps: List[str]
    competitors: List[Competitor]
    top_5_search_queries: List[SearchQuerySuggestion]
    seo_recommendations: SEORecommendations
    top_5_services: List[str]


class WebsiteData(BaseModel):
    url: str
    title: str
    description: str
    headings: List[str]
    content: str
    content_length: int


class LinkAnalysisData(BaseModel):
    website: WebsiteData
    analysis: WebsiteAnalysis


class LinkAnalysisResponse(BaseModel):
    success: bool
    data: LinkAnalysisData