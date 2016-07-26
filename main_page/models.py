# coding=utf-8
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
#from django.contrib.sites.models import Site


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class ServicesMain(models.Model):
    author = models.ForeignKey('auth.User')
    service_title = models.CharField(max_length=200)
    service_href = models.CharField(max_length=200, default='')
    service_is_deploy = models.BooleanField(default=False)
    service_display_serial_item = models.IntegerField(default=0)
    service_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.service_title


class ServiceItems(models.Model):
    author = models.ForeignKey('auth.User')
    service_item_text = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    service_main = models.ForeignKey(ServicesMain)
    service_cost = models.FloatField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # list_display =(self.service_item_text, self.service_main.service_title,)
        return '{0}|| {1}'.format(self.service_item_text, self.service_main.service_title)

        # return list_display
        # ' {0} | состоит в категории | {1}'.format(self.service_item_text, self.service_main.service_title)


class Contacts(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    mail_contact = models.EmailField()
    name_from_contact = models.CharField(max_length=200)

    def publish(self):
        self.created_date = timezone.now()
        self.save()


class BlogsItems(models.Model):
    author = models.ForeignKey('auth.User')
    blog_created_date = models.DateTimeField(default=timezone.now)
    blog_subject = models.CharField(max_length=250)
    blog_message = models.TextField()
    blog_is_deploy = models.BooleanField(default=False)

    def publish(self):
        self.blog_created_date = timezone.now()
        self.save()


class ServiceCart(models.Model):
    # Дата создание заказа
    created_date = models.DateTimeField(default=timezone.now)
    # адрес электронной почты заказчика
    mail_contakt = models.EmailField()
    # указанные услуги в заказе
    service_in_cart = models.ManyToManyField(ServiceItems, related_name="servincart")
    # общая стоимость заказа
    total_cost_service = models.FloatField(default=0)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    # class ServiceCartItems(models.Model):
    #    created_date = models.DateTimeField(default=timezone.now)
    #    service_in_cart = models.ForeignKey(ServiceItems)
    #    service_cart_main = models.ForeignKey(ServiceCart)

    # def publish(self):
    #    self.created_date = timezone.now()
    #    self.save()
