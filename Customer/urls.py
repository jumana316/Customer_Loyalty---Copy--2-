from django.urls import path
from .views import SignupView, UserDashboard, RewardsPage, LandingPage,date_filter

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'Customer'

urlpatterns = [
    path('', LandingPage, name='landing'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('UserDashboard/', UserDashboard, name='dashboard'),
    path('date_filter/', date_filter, name='date-filter'),
    path('rewards/', RewardsPage, name='rewards'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
]
