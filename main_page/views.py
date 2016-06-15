from django.shortcuts import render
from .models import ServicesMain, ServiceItems

# Create your views here.


def post_list(request):
    categ_service = ServicesMain.objects.all().order_by('service_title')
    service_items = ServiceItems.objects.all().order_by('service_main')
    return render(request, 'main_page/index.html', {"category_service": categ_service, "items": service_items})
