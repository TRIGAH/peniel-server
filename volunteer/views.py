from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView
from volunteer.serializers import VolunteerSerializer
from volunteer.models import Volunteer

# Create your views here.
class VolunteerCreateView(CreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer

class VolunteerListView(ListAPIView):
    queryset = Volunteer.objects.order_by('-date')
    serializer_class = VolunteerSerializer
	