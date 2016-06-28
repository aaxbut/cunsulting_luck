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


@csrf_exempt
def post_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
        try:
           # попытка проверки и записи формы в модель
            print(request.POST)  # тут разбираемся пу стой queryset приходит
            # pickup_records = {}
            pickup_records = {"success": 0, "status_text": "все хорошо"}


            pickup_records = {}
            pickup_records={ "success": 0 }
            #pickup_records.append({ "email_msg": request.POST['email']})
            #pickup_records.append({ "name_msg": request.POST['subject'] })

            # pickup_records.append({ "email_msg": request.POST['email']})
            # pickup_records.append({ "name_msg": request.POST['subject'] })
            # pickup_records.append({ "message_msg": request.POST['message'] })


            return HttpResponse(json.dumps(pickup_records), content_type="text/json")

            # contakt.subject =
        except BadHeaderError:  # Защита от уязвимости
            return HttpResponse('Invalid header found')
        #	#Переходим на другую страницу, если сообщение отправлено
        return render(request, 'main_page/index.html')
    return render(request, 'main_page/index.html')


def validation_feedbak(**kwargs):

    return True