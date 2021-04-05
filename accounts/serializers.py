from rest_framework import serializers
from django.contrib.auth.models import User

class login_serializer(serializers.Serializer):
    username = serializers.CharField(max_length=255,allow_blank=False)
    password = serializers.CharField(max_length=255, allow_blank=False)


class register_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, validated_data):
            print("create method")
            user = User.objects.create(username=validated_data.get('username'))
            print(validated_data.get('username'))
            user.set_password(validated_data.get('password'))
            print(validated_data.get('password'))
            user.save(  )
            return user



