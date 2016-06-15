from django.db import models
from django.utils import timezone
from django.utils.html import format_html


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
    service_column_rl = models.BooleanField(default=False)
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

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
       #list_display =(self.service_item_text, self.service_main.service_title,)
        return '{0}|| {1}'.format(self.service_item_text, self.service_main.service_title)

       # return list_display
        #' {0} | состоит в категории | {1}'.format(self.service_item_text, self.service_main.service_title)
