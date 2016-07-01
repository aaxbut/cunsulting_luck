import re
from email.utils import parseaddr


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
    print(res)
    return res
