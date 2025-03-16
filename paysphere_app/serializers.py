# # from rest_framework import serializers

# # class UserSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = User
# #         fields = '__all__'
# from rest_framework import serializers
# from .models import UserProfile

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
    

# from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user




# from rest_framework import serializers
# from .models import UserProfile
# from django.contrib.auth.hashers import make_password

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = UserProfile  # Use UserProfile instead of Django's default User model
#         fields = ['first_name', 'last_name', 'email', 'password', 'phone_no', 'dob', 'role', 'is_active']

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])  # Hash password
#         return UserProfile.objects.create(**validated_data)




# from rest_framework import serializers
# from .models import UserProfile
# from django.contrib.auth.hashers import make_password

# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
#         extra_kwargs = {'password': {'write_only': True}}  # Hide password in responses

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)

#     class Meta:
#         model = UserProfile
#         fields = ['first_name', 'last_name', 'email', 'password', 'phone_no', 'dob', 'role', 'is_active']

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])  # Hash password
#         return UserProfile.objects.create(**validated_data)

from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.hashers import make_password

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_no', 'dob', 'role', 'is_active']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
