
from django.contrib import admin
from django.urls import path,include
from .views import (MemberView,
                    ContactView,
                    EnquiryView,
                    EquipmentView,
                    PlanView)
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'Member',MemberView)
router.register(r'Contact',ContactView)
router.register(r'Enquiry',EnquiryView)
router.register(r'Equipment',EquipmentView)
router.register(r'Plan',PlanView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
