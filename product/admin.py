from django.contrib import admin
from .models import Requirement, Category, Product


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ["product", "email", "phone", "created_at", "addressed"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "code", "created_at"]
    list_filter = ["category"]