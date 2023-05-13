# Import default modules
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import password_validation
from django.contrib.auth.models import User


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    # fields to be serialized
    class Meta:
        model = User
        fields = ("id", "username", "email")


# SignUp Serializer
class SignUpSerializer(serializers.ModelSerializer):
    # Required fields for SignUp
    username = serializers.CharField(required=True, help_text="Username required")
    password = serializers.CharField(required=True, help_text="Password required")
    email = serializers.EmailField(required=True, help_text="Email required")
    
    # fields to be serialized
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    # Validate email for uniqueness
    def validate_email(self, email):
        user = User.objects.filter(email=email).first()
        if user:
            raise serializers.ValidationError("Email address already in use.")
        return email

    # Validate username for uniqueness
    def validate_username(self, username):
        user = User.objects.filter(username=username).first()
        if user:
            raise serializers.ValidationError("Use another username.")
        return username

    # Validate password by password_validation module
    def validate_password(self, password):
        password_validation.validate_password(password)
        return password

    # Serializer's response
    def to_representation(self, obj):
        ret = super(ModelSerializer, self).to_representation(obj)
    
    # Create new user with validated_data
    def create(self, validated_data):
        # Create user with fields( username, email, password)
        user = User.objects.create_user(
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


# SignIn Serializer
class SignInSerializer(serializers.ModelSerializer):
    # Required fields for SignUp
    username = serializers.CharField(required=True, help_text="Username required")
    password = serializers.CharField(required=True, help_text="Password required")

    # fields to be serialized
    class Meta:
        model = User
        fields = ("id", "username", "password")

    # Validate username for uniqueness
    def validate_username(self, username):
        user = User.objects.filter(username=username).first()
        if not user:
            raise serializers.ValidationError("Use another username.")
        return username

    # Validate password by password_validation module
    def validate_password(self, password):
        password_validation.validate_password(password)
        return password


# SignOut Serializer
class SignOutSerializer(serializers.Serializer):
    pass
