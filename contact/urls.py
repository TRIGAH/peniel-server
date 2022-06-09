from django.urls import path,include
from contact.views import ContactCreateView,ContactListView

urlpatterns = [
   
    path('api/contact-create/', ContactCreateView.as_view(), name='contact-create'),
    path('api/contact-list/', ContactListView.as_view(), name='contact-list'),

]