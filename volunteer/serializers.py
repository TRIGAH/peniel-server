from rest_framework import serializers
from volunteer.models import Volunteer

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'