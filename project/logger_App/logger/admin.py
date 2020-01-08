from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Customer,Sale,Product,Repair

class CustomerAdmin(admin.ModelAdmin):
    fields =  ('account','first_name','last_name','e_mail','customer_type','telephone','vat_id','address')
    list_display = ('account','first_name','last_name','e_mail','customer_type','telephone','vat_id','address','Products','Sales')

class myUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_customer',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('is_staff','is_customer',),
        }),
    )
    list_display = ('username','is_staff','is_customer')

admin.site.register(User, myUserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale)
admin.site.register(Repair)
admin.site.register(Product)
