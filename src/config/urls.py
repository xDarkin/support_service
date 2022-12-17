import json
from dataclasses import asdict, dataclass

from django.http import HttpResponse
from django.urls import path


@dataclass
class Person:
    name: str
    age: int


def get_john(variable):
    john = Person(name="John", age=30)
    content = json.dumps(asdict(john))
    content_type = "application/json"
    return HttpResponse(content, content_type=content_type)


urlpatterns = [
    path("john/", get_john),
]
