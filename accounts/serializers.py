from rest_framework import serializers
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom serializer for user registration to include optional first and last name fields.
    Overrides the default `get_cleaned_data` to handle first and last names.
    """
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def get_cleaned_data(self):
        """Returns cleaned data including first and last names (if provided) during registration."""
        data_dict = super().get_cleaned_data()
        data_dict['first_name'] = self.validated_data.get('first_name', '')
        data_dict['last_name'] = self.validated_data.get('last_name', '')
        return data_dict

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user details, including id, username, email, and name fields.
    Fields are read-only.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = fields