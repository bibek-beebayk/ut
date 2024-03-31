from django.contrib import admin
from .models import Requirement


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ["product", "email", "phone", "created_at", "addressed"]
