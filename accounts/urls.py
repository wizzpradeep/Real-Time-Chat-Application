from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('signin/', Signin.as_view(), name='signin'),
    path('logout/', log_out, name='logout'),
]