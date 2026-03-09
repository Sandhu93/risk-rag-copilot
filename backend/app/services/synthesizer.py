from app.models.schemas import Citation


class SynthesizerService:
    """Placeholder answer composer. Replace with LLM call later."""

    def compose_answer(self, question: str, context: list[Citation], sql_result: list[dict] | None) -> str:
        answer = f"Draft answer for: {question}."
        if sql_result:
            answer += " Included structured exposure snapshot from SQL tool."
        answer += " Replace this logic with an LLM response constrained to provided evidence."
        return answer
