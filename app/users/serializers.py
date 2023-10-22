from rest_framework import serializers
from .models import User
from .emails import send_verification
from rest_framework.exceptions import APIException

class baseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        try:
            send_verification(user)
            user.save()
        except Exception as exc:
            print(f"failed to save user, ERR: f{exc}")
            raise APIException(f"Failed to save user: {exc}")
        return user
    
    def update(self, instance, validated_data):
        print("hello")
        validated_data.pop("password")
        if 'avatar' in validated_data:
            instance.avatar = validated_data.pop('avatar')
        instance.save()
        return instance
