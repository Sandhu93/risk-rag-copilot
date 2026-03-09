# Tradeoff Notes (Template)

## Chunk size

- Smaller chunks: higher precision, more retrieval calls
- Larger chunks: more context per hit, risk of noise

## Retrieval strategy

- Dense only: simpler, weaker exact match
- Hybrid dense + keyword: better recall, more complexity

## Latency vs quality

- More retrieved docs and tool calls can improve quality but add latency
- Caching, smaller models, and staged pipelines can reduce latency
