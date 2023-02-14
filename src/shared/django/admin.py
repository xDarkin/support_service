from typing import List, Union

from django.contrib.admin import ModelAdmin

_FIELDS = ["created_at", "updated_at"]


class TimeStampReadonlyAdmin(ModelAdmin):
    readonly_fields = _FIELDS
    list_display: Union[List] = _FIELDS
    list_filter: Union[List] = _FIELDS
    search_fields = _FIELDS
