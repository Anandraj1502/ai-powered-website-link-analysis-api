# LLM Model Comparison – AI Website Link Analysis API

## 1. Objective

The purpose of this research is to evaluate Large Language Models (LLMs) suitable for website content analysis, business insight generation, competitor suggestions, and SEO recommendations.

The comparison focuses on response quality, latency, API cost, context capacity, structured output support, ease of integration, and suitability for the project.

## 2. Models Selected

| Model | Provider | Category |
|---|---|---|
| Gemini Flash family | Google | Fast, cost-efficient analysis |
| GPT mini family | OpenAI | General-purpose analysis |
| Claude Haiku 4.5 | Anthropic | Lightweight language analysis |

Model selection should be based on the exact API model identifier available at implementation time. Model availability and pricing can change.

## 3. Comparison Criteria

| Factor | Gemini Flash | GPT mini | Claude Haiku |
|---|---|---|---|
| Provider | Google | OpenAI | Anthropic |
| Response quality | Suitable for text analysis and structured generation | General-purpose language and reasoning tasks | Language understanding and summarization |
| Speed | Flash models are designed for efficient responses | Depends on selected model | Haiku models are lightweight |
| Cost | Depends on model and usage tier | Depends on model and usage tier | Depends on model and usage tier |
| Context window | Varies by exact model | Varies by exact model | Varies by exact model |
| Structured output | Supported by compatible models and API features | Supported by compatible models and API features | Structured output available through supported API features |
| Integration | Google GenAI SDK | OpenAI SDK | Anthropic SDK |

Speed and quality descriptions are qualitative assessments based on model positioning, not benchmarks conducted by this project.

## 4. Evaluation Criteria

### Response Quality

The model should identify the website's business, understand its target audience, summarize brand positioning, and provide relevant SEO and marketing suggestions.

### Response Speed

The API should return analysis within a reasonable time. Lower latency improves usability, particularly for interactive applications.

### Cost

The model should be affordable for repeated website analysis. Cost depends on input tokens, output tokens, model choice, and pricing tier.

### Structured Output

The model should generate consistent JSON that can be validated and consumed by the FastAPI application.

### Context Capacity

The model should support the extracted website text and analysis instructions within its context limits.

### Integration

The provider should offer a stable SDK and clear documentation for API calls, error handling, and structured responses.

## 5. Estimated Cost per Analysis

Assumptions for one analysis:

- Input tokens: 5,000
- Output tokens: 1,500

Cost formula:

**Estimated cost = (Input tokens × Input price + Output tokens × Output price) / 1,000,000**

Exact pricing is not included in this comparison because API rates depend on the specific model, usage tier, and provider pricing updates. Current prices should be checked using the official provider pricing pages before deployment.

## 6. Advantages and Limitations

### Gemini Flash

**Advantages**
- Designed for efficient response generation
- Suitable for text-based analysis
- Supports structured output options
- SDK integration with the Google GenAI library

**Limitations**
- AI-generated insights may contain inaccurate assumptions
- Competitor suggestions require independent verification
- Output validation is still necessary

### GPT mini

**Advantages**
- General-purpose language capabilities
- Suitable for structured analysis tasks
- Well-documented API ecosystem

**Limitations**
- Costs vary by model and usage tier
- AI-generated business claims may need verification
- Requires additional integration if used as an alternative provider

### Claude Haiku 4.5

**Advantages**
- Lightweight model family
- Useful for summarization and language analysis
- Supports API-based structured generation workflows

**Limitations**
- Pricing depends on API usage
- Generated recommendations may require manual review
- A separate SDK and integration would be needed

## 7. Selected Model

**Selected model: Google Gemini**

Gemini was selected for this project because it provides an accessible API, supports structured response generation, and can be integrated using Google's GenAI SDK.

The project uses Gemini to analyze extracted website content and generate business insights, competitor suggestions, search queries, and SEO recommendations.

This workload primarily involves webpage text analysis and structured generation, making a Flash-family model an appropriate starting point.

The deployed API was tested successfully and returned structured analysis with HTTP 200 OK.

## 8. Cost Optimization

Potential cost optimization techniques include:

- Limit extracted website content to a reasonable size.
- Remove scripts, styles, and unnecessary HTML.
- Use concise prompts.
- Request only required output fields.
- Use a lower output token limit when appropriate.
- Cache results for repeated website analysis.
- Avoid duplicate AI calls when website content has not changed.
- Select a model based on actual quality and cost testing.

## 9. Reliability and Fallback Strategy

To improve reliability:

- Validate AI responses using Pydantic schemas.
- Handle timeouts and provider errors.
- Return clear errors when the AI provider