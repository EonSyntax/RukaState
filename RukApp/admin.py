from django.contrib import admin
from .models import Property, Address, PropertyImage, ContactMessage
# Register your models here.


class AddressInLine(admin.StackedInline):
    model = Address
    can_delete = False
    verbose_name_plural = 'Address'


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street','city','state','postal_code','country')  
    search_fields = ('street','city','state','postal_code','country') 

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1 # how many empty image forms to show  
    verbose_name_plural = 'PropertyImages'

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject')