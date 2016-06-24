from django.contrib import admin
from .models import Post, ServiceItems, ServicesMain, Contacts

admin.site.register(Post)


class ServicesItemsAdmin(admin.ModelAdmin):
    list_display = ('service_item_text', 'service_main')


class ServiceMainAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_is_deploy', 'service_display_serial_item')


# определяем вид представления в админке Контактов
class ContactViewAdmin(admin.ModelAdmin):
    list_display = ('name_from_contact', 'mail_contact', 'subject', 'created_date')


admin.site.register(ServiceItems, ServicesItemsAdmin)
admin.site.register(ServicesMain, ServiceMainAdmin)
admin.site.register(Contacts, ContactViewAdmin)
