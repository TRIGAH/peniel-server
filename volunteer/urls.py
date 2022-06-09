from django.urls import path,include
from volunteer.views import VolunteerCreateView,VolunteerListView

urlpatterns = [
   
    path('api/volunteer-create/', VolunteerCreateView.as_view(), name='volunteer-create'),
    path('api/volunteer-list/', VolunteerListView.as_view(), name='volunteer-list'),

]