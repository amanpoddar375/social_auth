from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from allauth.socialaccount.models import SocialAccount
from django.shortcuts import redirect


def login_view(request):
    """Renders the login page or redirects to the profile page if the user is authenticated."""
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'login.html')

@login_required
def profile_view(request):
    """
    Renders the profile page and displays the user's social provider if linked.
    Defaults to 'standard' if no social account is found.
    """
    try:
        social_account = SocialAccount.objects.filter(user=request.user).first()
        provider = social_account.provider if social_account else 'standard'
    except:
        provider = 'standard'
    
    return render(request, 'home.html', {'provider': provider})

class UserInfoAPIView(APIView):
    """
    Returns authenticated user's info, including social account data if available.
    Requires token authentication and the user to be logged in.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieves and returns the user's ID, username, email, full name, and social account data."""
        user = request.user
        try:
            social_account = SocialAccount.objects.filter(user=user).first()
            provider = social_account.provider if social_account else None
            extra_data = social_account.extra_data if social_account else {}
        except:
            provider = None
            extra_data = {}
        
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'auth_provider': provider,
            'social_data': extra_data
        }
        
        return Response(data, status=status.HTTP_200_OK)