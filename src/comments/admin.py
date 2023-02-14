from comments.models import Comment
from django.contrib import admin
from shared.django import TimeStampReadonlyAdmin


@admin.register(Comment)
class CommentsAdmin(TimeStampReadonlyAdmin):
    list_display = ["body", "id", "ticket", "user"]
    list_filter = ["user", "ticket"]
    search_fields = ["body"]
