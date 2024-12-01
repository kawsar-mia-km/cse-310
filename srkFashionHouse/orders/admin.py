from django.contrib import admin

from orders.views import create_order, order_success

# Register your models here.
admin.site.register(create_order)
admin.site.register(order_success)