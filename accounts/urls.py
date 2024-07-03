from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomSignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
    path('signup/', CustomSignUpView.as_view(), name='signup'),
]
