from django.urls import path
from . import views
from users.views import ProfileView,SecurityView,SocialView,NotificationView, LanguagesView, SignUpView, EducationView, SkillView
app_name = 'users'
urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logOut, name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('signup/success', views.signup_save, name='signup_save'),
    path(r'settings/<str:username>/', ProfileView.as_view(), name='profile'),
    path(r'settings/<str:username>/update/', views.update_profile),
    
    path(r'settings/<str:username>/notification/', NotificationView.as_view(), name='profileNotification'),
    
    path(r'settings/<str:username>/security/', SecurityView.as_view(), name='profileSecurity'),
    path(r'settings/<str:username>/security/update/', views.update_security_profile),
    #social-network-settings
    path(r'settings/<str:username>/social-network/', SocialView.as_view(), name='profileSocialNetwork'),
    path(r'settings/<str:username>/social-network/update/', views.update_social_profile, name='updateSocialProfile'),
    #languages-settings
    path(r'settings/<str:username>/languages/', LanguagesView.as_view(), name='profilelanguages'),
    #skills-settings
    path(r'settings/<str:username>/skills/', SkillView.as_view(), name='profileSkill'),
    path(r'settings/<str:username>/skills/add/', views.add_skill_save, name="add_skill_save"),
    
    
    path(r'settings/<str:username>/education/', EducationView.as_view(), name='profileEducation'),
    path(r'settings/<str:username>/education/update/', views.save_education, name="updateEducation"),
    path(r'settings/<str:username>/education/delete/<int:pk>/',views.delete_education, name="deleteEducation"),
    
    
    # path('signup', SignupView.as_view(), name="signup"),
]
