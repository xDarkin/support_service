import json

import requests
from django.conf import settings
from django.http import JsonResponse

from .services import AlphavantageResponse


def convert(request):
    currencies = json.loads(request.body)
    from_cur = currencies["from"]
    to_cur = currencies["to"]
    url = (
        f"{settings.ALPHA_VANTAGE_BASE_URL}/query?"
        f"function=CURRENCY_EXCHANGE_RATE&from_currency={from_cur}"
        f"&to_currency={to_cur}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    )
    response = requests.get(url)
    alphavantage_response = AlphavantageResponse(**response.json())
    res = alphavantage_response.dict()["results"]
    res["exchange_rate"] = float("{:.3f}".format(float(res["exchange_rate"])))
    return JsonResponse(res)
