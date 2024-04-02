from django.contrib import admin
from .models import ContactUs, Requirement, Category, Product


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ["product", "email", "phone", "created_at", "addressed"]
    readonly_fields = ["product", "email", "phone"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "code", "created_at"]
    list_filter = ["category"]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "message", "is_addressed"]
    readonly_fields = ["name", "email", "phone", "message"]