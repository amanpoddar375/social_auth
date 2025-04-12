# This file contains a custom adapter for handling social account logins.
# Currently, it's not in use as the default functionality of django-allauth is sufficient.
# uncomment or modify this file if need to customize the social login behavior 
# (e.g., to add custom user fields, modify the login process, etc.).

# For now, this file is not being used in the project.

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Custom adapter to modify the social login process.

    Methods:
    1. `pre_social_login(request, sociallogin)`:
        Custom logic before the user logs in via a social account. Use this to add checks or modify the login request.
    2. `populate_user(request, sociallogin, data)`:
        Custom logic for populating the user model with data from the social account provider. Modify how the user data is populated from the social login.

    Example Use Cases:
    - Block login for specific users based on social profile info.
    - Populate custom fields in the user model (e.g., profile picture, address).
    """
    def pre_social_login(self, request, sociallogin):
        """
        Custom logic before social login.
        Can be used for conditions or modifying the login request.
        """
        # Custom logic before social login
        pass

    def populate_user(self, request, sociallogin, data):
        """
        Customize user population from social login data.
        Add extra logic to modify user fields.
        """
        user = super().populate_user(request, sociallogin, data)
        # Add custom user population logic here
        return user