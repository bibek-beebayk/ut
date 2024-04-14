from django.shortcuts import render
from product.models import Category, ContactUs, Product, Quote, Requirement
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
    paginator = Paginator(queryset, 30)  # 10 products per page
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


def about_us(request):
    context = {}
    return render(request, "about.html", context)


def contact_us(request):
    context = {}
    if request.method == "POST":
        contact_data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "message": request.POST.get("message")
        }
        ContactUs.objects.create(**contact_data)
        messages.success(request, "Your message was submitted successfully. We will get back to you in a while.")
    return render(request, "contact.html", context)


def quote(request):
    context = {}
    # if request.method == "POST":
    #     quote_data = {
    #         "name": request.POST.get("name"),
    #         "email": request.POST.get("email"),
    #         "phone": request.POST.get("phone"),
    #         "delivery_date": request.POST.get("delivery_date"),
    #         "message": request.POST.get("message")
    #     }
    #     Quote.objects.create(**quote_data)
    #     messages.success(request, "Your quote was submitted successfully. We will get back to you in a while.")
    return render(request, "quote.html", context)