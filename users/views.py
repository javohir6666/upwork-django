from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here..
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser == True:
                return render(request, 'pages/index.html')
            return redirect("index")
        else:
            return HttpResponse("Username or password is incorrect")

    return render(request, 'users/login.html')

def logOut(request):
    logout(request)
    return redirect('users:login')


class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'users/profile/edit_profile.html', {"customuser": user})
    
    
def update_profile(request, username):
        if request.method != "POST":
            HttpResponse('Method not allowed!')
        else:         
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            about = request.POST.get("about")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            gender = request.POST.get("gender")
            
            try:
                user = get_object_or_404(CustomUser, username=username)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.about = about
                user.address = address
                user.phone = phone
                user.gender = gender
                user.save()
                messages.success(request, "Account has been updated!")
            except:
                messages.error(request, "Failed to updating account")
            return redirect(request.META.get("HTTP_REFERER"))
    
    
    
    
class SecurityView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'users/profile/security.html', {"customuser": user})
    
    
class SocialView(View, LoginRequiredMixin):
    login_url = 'users:login'
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'users/profile/social_profiles.html', {"customuser": user})


def update_social_profile(request, username):
        if request.method != "POST":
            HttpResponse('Method not allowed!')
        else:         
            telegram = request.POST.get("telegram")
            instagram = request.POST.get("instagram")
            facebook = request.POST.get("facebook")
            linkedin = request.POST.get("linkedin")
            github = request.POST.get("github")
            
            try:
                user = get_object_or_404(CustomUser, username=username)
                user.telegram = telegram
                user.instagram = instagram
                user.facebook = facebook
                user.linkedin = linkedin
                user.github = github
                user.save()
                messages.success(request, "Account has been updated!")
            except:
                messages.error(request, "Failed to updating account")
            return redirect(request.META.get("HTTP_REFERER"))
    
class NotificationView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'users/profile/notifications.html', {"customuser": user})