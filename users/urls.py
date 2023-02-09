from django.urls import path
from . import views
from users.views import ProfileView,SecurityView,SocialView,NotificationView
app_name = 'users'
urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/update/', views.update_profile),
    path('profile/<str:username>/notification/', NotificationView.as_view(), name='profileNotification'),
    path('profile/<str:username>/security/', SecurityView.as_view(), name='profileSecurity'),
    path('profile/<str:username>/social-network/', SocialView.as_view(), name='profileSocialNetwork'),
    path('profile/<str:username>/social-network/update/', views.update_social_profile, name='updateSocialProfile'),
    # path('signup', SignupView.as_view(), name="signup"),
]
