from django.contrib import admin
from .models import signup,ClientDetails,DailyUpdate #,Order,Customer,Payment
# Register your models here.

admin.site.register(signup)
admin.site.register(ClientDetails)
admin.site.register(DailyUpdate)

'''
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Payment)


'''
