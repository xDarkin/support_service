from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    exchange_rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")
