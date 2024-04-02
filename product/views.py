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


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def products(request):
    context = {}
    context["categories"] = Category.objects.all()
    queryset = Product.objects.order_by("-created_at")
    category_id = request.GET.get("category")
    if category_id:
        queryset = queryset.filter(category_id=category_id)

    # Pagination
    paginator = Paginator(queryset, 2)  # 10 products per page
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        products = paginator.page(paginator.num_pages)
    context["products"] = products      
    return render(request, "products.html", context)