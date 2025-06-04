from django.contrib import admin
from service.models import service
class serviceadmin(admin.ModelAdmin):
    list_display=('service_ID','service_Title','service_Desc')
admin.site.register(service,serviceadmin)

# Register your models here.
