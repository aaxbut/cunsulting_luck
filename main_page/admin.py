from django.contrib import admin
from .models import Post, ServiceItems, ServicesMain, Contacts, ServiceCart\
    #, ServiceCartItems

admin.site.register(Post)


class ServicesItemsAdmin(admin.ModelAdmin):
    list_display = ('service_item_text', 'service_main')


class ServiceMainAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'service_is_deploy', 'service_display_serial_item')


# определяем вид представления в админке Контактов
class ContactViewAdmin(admin.ModelAdmin):
    list_display = ('name_from_contact', 'mail_contact', 'subject', 'created_date')

# определяем представление главной карточки заказа
class ServiceCartViewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mail_contakt', 'created_date', 'total_cost_service')
    filter_horizontal = ('service_in_cart',)


# определяем представление табличной части заказа
#class ServiceCartItemsViewAdmin(admin.ModelAdmin):
#    list_display = ('pk', 'mail_contakt', 'created_date')

admin.site.register(ServiceItems, ServicesItemsAdmin)
admin.site.register(ServicesMain, ServiceMainAdmin)
admin.site.register(Contacts, ContactViewAdmin)
admin.site.register(ServiceCart, ServiceCartViewAdmin)
#admin.site.register(ServiceCartItems, ServiceCartItemsViewAdmin)
