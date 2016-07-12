from django.shortcuts import render
from .models import ServicesMain, ServiceItems, Contacts
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import BadHeaderError
import json
from .validate_feedback import valid_feedback
# Create your views here.
from django import forms


def post_list(request):
    categ_service = ServicesMain.objects.filter(service_is_deploy=True).order_by('service_display_serial_item')
    service_items = ServiceItems.objects.all().order_by('service_main')
    return render(request, 'main_page/index.html', {"category_service": categ_service, "items": service_items})


def certs(request):
    return render(request, 'main_page/certs.html')


@csrf_exempt
def post_contact(request):
    if request.method == 'POST':
        try:
            # попытка проверки и записи формы в модель

            print(request.POST)  # тут разбираемся пу стой queryset приходит
            pickup_records = valid_feedback(email_msg=request.POST['email'], subj_message=request.POST['subject'],
                                            message_msg=request.POST['message'], name_sender=request.POST['name'],
                                            csrf_token=request.POST['csrfmiddlewaretoken'])
            return HttpResponse(json.dumps(pickup_records), content_type="text/json")
        except BadHeaderError:  # Защита от уязвимости
            return HttpResponse('Invalid header found')
        # #Переходим на другую страницу, если сообщение отправлено
        return render(request, 'main_page/index.html')
    return render(request, 'main_page/index.html')

@csrf_exempt
def cost_service(request):
    print(request.POST)
    categ_service = ServicesMain.objects.filter(service_is_deploy=True).order_by('service_display_serial_item')
    service_items = ServiceItems.objects.all().order_by('service_main')
    return render(request, 'main_page/costserv.html',{"category_service": categ_service, "items": service_items})
