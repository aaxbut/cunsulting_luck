from django.shortcuts import render
from .models import ServicesMain, ServiceItems, Contacts
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import BadHeaderError
import json
from .validate_feedback import valid_feedback
# Create your views here.
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	sender = forms.EmailField()
	message = forms.CharField()

def post_list(request):
    categ_service = ServicesMain.objects.filter(service_is_deploy=True).order_by('service_display_serial_item')
    service_items = ServiceItems.objects.all().order_by('service_main')
    if request.method == 'POST':
        print('++')
    return render(request, 'main_page/index.html', {"category_service": categ_service, "items": service_items})

@csrf_exempt
def post_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
        try:
			#		send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
            print(request.POST) # тут разбираемся пустой queryset приходит
            contakt = Contacts()

            pickup_records = {}
            pickup_records={ "success": 0 }
            valid_feedback(email_msg=request.POST['email'], subj_message=request.POST['subject'], message_msg = request.POST['message'], name_sender = request.POST['name'], csrf_token = request.POST['csrfmiddlewaretoken'] )
            #pickup_records.append({ "email_msg": request.POST['email']})
            #pickup_records.append({ "name_msg": request.POST['subject'] })
            #pickup_records.append({ "message_msg": request.POST['message'] })

            return HttpResponse(json.dumps(pickup_records), content_type="text/json")

            #contakt.subject =
        except BadHeaderError: #Защита от уязвимости
            return HttpResponse('Invalid header found')
			#	#Переходим на другую страницу, если сообщение отправлено
        return render(request, 'main_page/index.html')
        print('++')
    return render(request, 'main_page/index.html')
					# def post_contact(request):#

	#		return ""
   #    #
#			form = ContactForm(request.POST)#
		#Если форма заполнена корректно, сохраняем все введённые пользователем значения
	#		if form.is_valid():
#				subject = form.cleaned_data['subject']#
				#sender = form.cleaned_data['sender']
				#message = form.cleaned_data['message']
				#recipients = ['ВАШ_EMAIL_ДЛЯ_ПОЛУЧЕНИЯ_СООБЩЕНИЯ']
				#Если пользователь захотел получить копию себе, добавляем его в список получателей
				#if copy:
			#		recipients.append(sender)
			#	try:
			#		send_mail(subject, message, 'ВАШ_EMAIL_ДЛЯ_ОТПРАВКИ_СООБЩЕНИЯ', recipients)
			#	except BadHeaderError: #Защита от уязвимости
			#		return HttpResponse('Invalid header found')
			#	#Переходим на другую страницу, если сообщение отправлено
			#	return render(request, 'site/thanks.html')
	#		else:
	#			#Заполняем форму
	#			form = ContactForm()
	#	#Отправляем форму на страницу
	#	#return render(request, 'site/contact.html', {'form': form})
     #   return print(request.method)