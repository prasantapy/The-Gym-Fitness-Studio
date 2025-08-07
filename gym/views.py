from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import( IsAuthenticated,
                                       AllowAny,
                                       IsAuthenticatedOrReadOnly,)
from rest_framework.authentication import (TokenAuthentication,
                                           BaseAuthentication)

from gym.models import (Member,
                        Contact,
                        Enquiry,
                        Equipment,
                        Plan)
from gym.serializer import(MemberSerializer,
                            ContactSerializer,
                            EnquirySerializer,
                            EquipmentSerializer,
                            PlanSerializer,)

class MemberView(ModelViewSet):  
    queryset = Member.objects.all()
    serializer_class = MemberSerializer  
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ContactView(ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class EnquiryView(ModelViewSet):

    queryset=Enquiry.objects.all()
    serializer_class=EnquirySerializer
    authentication_classes=[]
    permission_classes=[AllowAny]

class EquipmentView(ModelViewSet):
    queryset=Equipment.objects.all()
    serializer_class=EquipmentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class PlanView(ModelViewSet):
    queryset=Plan.objects.all()
    serializer_class=PlanSerializer
    authentication_classes=[]
    permission_classes=[AllowAny]