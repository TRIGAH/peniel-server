from django.shortcuts import render
from contact.models import Contact
from rest_framework.generics import CreateAPIView,ListAPIView
from contact.serializers import ContactSerializer

# Create your views here.
class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactListView(ListAPIView):
    queryset = Contact.objects.order_by('-date')
    serializer_class = ContactSerializer
	