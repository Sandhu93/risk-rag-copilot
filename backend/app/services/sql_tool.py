class SQLToolService:
    """Placeholder SQL tool service."""

    def run_query(self, question: str) -> tuple[str | None, list[dict] | None]:
        # TODO: add NL->SQL and SQL safety checks.
        if "exposure" in question.lower():
            query = "SELECT counterparty, exposure_usd FROM exposures ORDER BY exposure_usd DESC LIMIT 5;"
            result = [
                {"counterparty": "ABC Capital", "exposure_usd": 12000000},
                {"counterparty": "Zenith Bank", "exposure_usd": 9500000},
            ]
            return query, result
        return None, None
