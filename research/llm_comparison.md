# LLM Model Comparison – AI Website Link Analysis API

## 1. Objective

The purpose of this research is to compare three LLMs suitable for website content analysis, business insight generation, competitor suggestions, and SEO recommendations.

The comparison focuses on response quality, speed, pricing, context window, JSON output support, and ease of integration.

## 2. Models Selected

| Model | Provider | Category |
|---|---|---|
| Gemini 3.5 Flash-Lite | Google | Fast, cost-efficient |
| GPT-5.4 mini | OpenAI | Balanced performance |
| Claude Haiku 4.5 | Anthropic | Lightweight analysis |

## 3. Comparison

| Factor | Gemini 3.5 Flash-Lite | GPT-5.4 mini | Claude Haiku 4.5 |
|---|---|---|---|
| Provider | Google | OpenAI | Anthropic |
| Quality | Suitable for structured analysis | Strong general-purpose capability | Strong language and analysis capability |
| Speed | Designed for low latency | Balanced speed and performance | Fast lightweight model |
| Input pricing / 1M tokens | $0.30 | $0.75 | $1.00 |
| Output pricing / 1M tokens | $2.50 | $4.50 | $5.00 |
| Context window | ~1M tokens | ~400K tokens | ~200K tokens |
| JSON support | Supported | Supported | Supported |
| Integration | Google GenAI SDK | OpenAI SDK | Anthropic SDK |

*Pricing and context figures are approximate research values and should be verified on official provider pricing pages before deployment. Speed and quality descriptions are qualitative, not benchmark measurements performed by this project.*

## 4. Evaluation Criteria

### Response Quality
The model should accurately identify a website's business, understand its audience, summarize its positioning, and produce useful SEO suggestions.

### Response Speed
A shorter response time improves the user experience. Website analysis should complete within a reasonable time without unnecessarily long AI output.

### Cost
The API should remain affordable for repeated website analysis requests.

### Structured Output
The model must return valid JSON so the response can be used by the FastAPI application without manual parsing.

### Context Capacity
The model should support enough input text to analyze extracted website content.

## 5. Estimated Cost per Analysis

Assumption for one analysis:

- Input: 5,000 tokens
- Output: 1,500 tokens

| Model | Estimated cost per analysis |
|---|---:|
| Gemini 3.5 Flash-Lite | $0.00525 |
| GPT-5.4 mini | $0.0105 |
| Claude Haiku 4.5 | $0.0125 |

These are estimates based on standard per-token rates and the assumed token usage. Actual costs depend on token consumption, current pricing, and additional provider charges.

## 6. Advantages and Limitations

### Gemini 3.5 Flash-Lite
**Advantages**
- Cost-efficient for repeated analysis
- Supports structured JSON output
- Suitable for website text analysis
- Large context capacity

**Limitations**
- AI suggestions may be inaccurate
- Competitor identification may require external search verification
- Output must be validated

### GPT-5.4 mini
**Advantages**
- Strong general-purpose model
- Useful for complex reasoning and structured tasks
- Flexible API ecosystem

**Limitations**
- Higher estimated cost than the selected Gemini model
- Output can still contain unsupported assumptions

### Claude Haiku 4.5
**Advantages**
- Good language understanding and summarization
- Suitable for business content analysis
- Structured output can be implemented through constrained tool/schema approaches

**Limitations**
- More expensive under the comparison assumptions
- AI-generated insights still require validation

## 7. Selected Model

**Selected model: Gemini 3.5 Flash-Lite**

Google Gemini was selected for this project because it offers a good balance of affordability, speed-oriented design, large context capacity, and JSON output support.

The project uses the Google GenAI SDK to analyze extracted website information and return structured business and SEO insights. The API was tested successfully with a website, and it returned a valid JSON response with HTTP 200 OK.

The model is suitable for this practical test because the workload mainly involves analyzing text and generating structured recommendations rather than performing complex reasoning tasks.

## 8. Cost Optimization

The following techniques can help reduce API cost:

- Limit extracted website content to a reasonable size.
- Avoid sending unnecessary HTML, scripts, styles, and navigation text.
- Keep the AI prompt concise and specific.
- Request only the fields needed by the API.
- Use a low temperature for more consistent responses.
- Cache results for repeated analysis of the same website when appropriate.
- Avoid repeated AI calls for the same input unless the content changes.

## 9. Reliability and Fallback Strategy

To improve reliability:

- Validate AI output using Pydantic models.
- Handle API timeouts and provider errors.
- Return a clear error response when the AI provider is unavailable.
- Retry only temporary failures and limit retries.
- Consider a secondary model/provider as a future fallback.
- Label AI-inferred competitors and recommendations so they are not presented as verified facts.

A secondary provider has not yet been implemented in this version.

## 10. Research Sources

- Gemini model information and evaluation: https://deepmind.google/models/
- Gemini API documentation: https://ai.google.dev/gemini-api/docs
- OpenAI API documentation: https://platform.openai.com/docs/models
- Anthropic model documentation: https://docs.anthropic.com/en/docs/about-claude/models/overview
- Model comparison and pricing reference: https://www.dailyaiintel.com/tools/model-comparison

*Prices and model specifications are subject to change. The figures above are a research snapshot, not a live quote.*
