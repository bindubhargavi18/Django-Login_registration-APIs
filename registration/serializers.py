from rest_framework import serializers
from .models import UserDetails


class UserDetailsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)

    class Meta:
        model = UserDetails
        fields = ['username', 'password', 'email', 'city', 'state']

    def create(self, validated_data):
        user = UserDetails.objects.create_user(validated_data['username'], validated_data['email'],validated_data['password'],
                                               city=validated_data['city'], state=validated_data['state'])
        return user
