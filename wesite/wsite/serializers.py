from rest_framework import serializers
from wsite.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'link', 'count_sub', 'username', 'email')

class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = ('name', 'id', 'weather_data')

class SubSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscriptions
        fields = ('user_name', 'city_name', 'time')