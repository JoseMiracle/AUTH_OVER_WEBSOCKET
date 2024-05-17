from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=9, write_only=True)


    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'password',
            'email',
            'username'
        ] 
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]
    
class LoginInSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        """
        This is for validating the values provided by user to login
        """
        user = User.objects.filter(email=attrs["email"]).first()

        error = {}
        if (user and user.check_password(attrs["password"])) and (
            user.is_active == True
        ):
            return user

        else:
            error["credential_error"] = "Please recheck the credentials provided."
            raise serializers.ValidationError(error)                

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "refresh": str(refresh),
            "access_token": str(refresh.access_token),
            "profile": ProfileSerializer(instance).data
        }