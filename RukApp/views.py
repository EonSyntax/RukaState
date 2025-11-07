from django.shortcuts import render, get_object_or_404
from .models import Property
from .forms import ContactMessage
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    property = Property.objects.order_by('-created_at')[:6]
    return render(request, 'pages/index.html', {'property':property})

def about(request):
    return render(request, 'pages/About.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            number=phone,
            subject=subject,
            message=message
        )
    return render(request, 'pages/contact.html')



def blog(request):
    return render(request, 'pages/blog.html')

def properties(request):
    property = Property.objects.all().order_by('-id')
    paginator = Paginator(property, 6)  # Show 6 properties per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        # important: do not pass "property" anymore
        # use page_obj instead in template
    }


    return render(request, 'pages/properties.html', context)


def property_details(request, pk):
    property_details = get_object_or_404(Property, pk=pk)
    return render(request, 'pages/property-details.html', {'property_details':property_details}) 

def blog_details(request):
    return render(request, 'pages/blog-details.html') 

