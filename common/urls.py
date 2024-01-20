from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'common'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', logout_page, name='logout'),
    path('accounts/', include('allauth.urls')),
    
]

#localhost:8000/accounts/github/login
#localhost:8000/accounts/google/login
#localhost:8000/accounts/naver/login
#localhost:8000/accounts/kakao/login