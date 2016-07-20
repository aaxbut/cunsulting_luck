import re
from .models import ServiceCart, ServiceItems, Contacts
from django.utils import timezone
from email.utils import parseaddr
import pickle

def valid_feedback(**kwargs):
    res = {}
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', kwargs.get('email_msg'))
    if match is None:
        # print('Bad Syntax')
        res = {"success": 0}
    else:
        res = {"success": 1}
    print('проверка имени')
    if len(kwargs.get('name_sender')) < 2:
        res = {'name_sender': 'необходимо ввести имя'}
    else:
        print(len(kwargs.get('name_sender')), kwargs.get('name_sender'))
        # if  kwargs.get('name_sender') == None:
        #    print(kwargs.get('name_sender'))
        # else:
        #    res={"success":1}
        # if  kwargs.get('message_msg') == None:
        #    print('напишите текст')
        # else:
        #    res={"success":1}
        # if  kwargs.get('subj_message') == None:
        #    print('напишите тему сообщения')
        # else:
        #    print(res)

        #   raise ValueError('Bad Syntax')
        #   email_msg, subj_message, message_msg, name_sender, csrf_token)
    if res['success'] == 1:
        feedback_items = Contacts()
        feedback_items.created_date = timezone.now()
        feedback_items.mail_contact = kwargs.get('email_msg')

        #email_msg=request.POST['email'], subj_message=request.POST['subject'],
        #                                    message_msg=request.POST['message'], name_sender=request.POST['name'],
        #                                    csrf_token=request.POST['csrfmiddlewaretoken'])

        feedback_items.name_from_contact = kwargs.get('name_sender')
        feedback_items.message = kwargs.get('message_msg')
        feedback_items.subject = kwargs.get('subj_message')
        feedback_items.save()


        print('сохраняем данный для отправки почта')

    else:
        pass

    print(res)
    return res


def create_service_form_date(*args):
    items_in_cart = ServiceCart()
    items = ServiceItems.objects
    result = dict(args[0])
    # print(result)
    email_cart = result.pop('email_form_calc')
    csrf_cart = result.pop('csrfmiddlewaretoken')
    # print(result, "e-mail:", email_cart, "csrf : ", csrf_cart)
    # print("осталась только таб часть", result)
    # items_in_cart.
    items_in_cart.created_date = timezone.now()
    items_in_cart.mail_contakt = email_cart[0]
    # result = list(result)
    total_cost_in_cart = 0
    #servicecart.objects
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_cart[0])
    if match is None:
        # print('Bad Syntax')
        res = {"success1": 0}
    else:
        res = {"success1": 1}

        items_in_cart.save()
        for x in result:

            items_in_cart.service_in_cart.add(items.get(id=x).pk)
            total_cost_in_cart = total_cost_in_cart + items.get(id=x).service_cost
            print(x)
        items_in_cart.total_cost_service = float(total_cost_in_cart)
        print("Общая стоимость : ", total_cost_in_cart, res)
        items_in_cart.save()
    print (res)
    return res
