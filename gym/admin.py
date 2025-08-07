from django.contrib import admin

from .models import Contact, Enquiry, Equipment, Member, Plan
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'emailid', 'contact', 'subject', 'msgdate', 'isread')
    search_fields = ('name', 'emailid', 'subject')

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'age', 'gender')
    search_fields = ('name', 'email', 'mobile')
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit', 'purchasedate', 'description')
    search_fields = ('name', 'price')
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'gender', 'plan', 'joindate', 'initamount')
    search_fields = ('name', 'email', 'contact')
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'duration')
    search_fields = ('name', 'amount')