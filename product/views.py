from django.shortcuts import render
from product.models import Category, Product, Requirement
from django.contrib import messages

# Create your views here.

def index(request):
    context = {}
    if request.method=="POST":
        request_data = request.POST
        if request_data["type"] == "requirement":
            product_name = request_data.get("product_name")
            email = request_data.get("email")
            phone = request_data.get("phone")
            req = Requirement.objects.create(product=product_name, email=email, phone=phone)
            messages.success(request, "Your requirement was submitted successfully. We will contact you shortly.")
    context["categories"] = Category.objects.all()
    return render(request, "index.html", context)


def products(request):
    context = {}
    products = Product.objects.order_by("-created_at")
    context["products"] = products
    return render(request, "products.html", context)