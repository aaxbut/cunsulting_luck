from django.contrib import admin
from .models import Post, ServiceItems, ServicesMain, Contacts

admin.site.register(Post)
admin.site.register(Contacts)
#admin.site.register(ServicesMain)


class ServicesItemsAdmin(admin.ModelAdmin):
    list_display = ('service_item_text', 'service_main')


class ServiceMainAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_is_deploy', 'service_display_serial_item')

admin.site.register(ServiceItems, ServicesItemsAdmin)
admin.site.register(ServicesMain, ServiceMainAdmin)