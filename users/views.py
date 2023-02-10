from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import CustomUser, Education, Skill
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
            if not user.first_name:
                messages.info(request,"Please enter your information")
                return redirect("users:profile", username)
                
                
            return redirect("index")
        else:
            return messages.error("Username or password is incorrect")

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
    
    
def update_security_profile(request, username):
    if request.method != "POST":
        HttpResponse('Method not allowed!')
    else:
        current_password = request.POST.get("current_password")
        password = request.POST.get("password")
        if password == request.POST.get("password2"):
            try:
                user = get_object_or_404(CustomUser, username=username)
                user.password = password
                user.save()
                messages.success(request, "Password has been updated!")
            except:
                messages.error(request, "Failed to updating password")
            return redirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "Current password is incorrect or new password does not match")
            return redirect(request.META.get("HTTP_REFERER"))
    
        
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
    
class NotificationView(View, LoginRequiredMixin):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'users/profile/notifications.html', {"customuser": user})
    
    
class LanguagesView(View, LoginRequiredMixin):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'users/profile/Languages.html', {"customuser": user})
    
class EducationView(View, LoginRequiredMixin):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        educations = Education.objects.filter(author = user)
        return render(request, 'users/profile/education/education.html', {"customuser": user, 'educations': educations,})


def save_education(request,username):
    if request.method != "POST": 
        return HttpResponse("Method not allowed")
    else:
        title = request.POST.get('title')
        level = request.POST['level']
        name_of_deegree = request.POST.get('name_of_deegree')
        start = request.POST.get('start')
        end = request.POST.get('end')
        try:
            education = Education.objects.create(
                author = request.user,
                title = title,
                level = level,
                name_of_deegree = name_of_deegree,
                start = start,
                end = end
            )
            education.save()
            messages.success(request,"Education successfully added")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Sorry, something went wrong")
            return redirect(request.META.get("HTTP_REFERER"))


def delete_education(request,username, pk):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        Education.objects.filter(pk=pk).delete()
        messages.success(request,"Education successfully deleted")
        return redirect(request.META.get("HTTP_REFERER"))
            
            
class SkillView(View, LoginRequiredMixin):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        return render(request, 'users/profile/skill/detail.html', {"customuser": user})


def add_skill_save(request, username):
    if request.method != "POST": 
        return HttpResponse("Method not allowed")
    else:
        title = request.POST.get('title')
        try:
            skill = Skill.objects.create(
                author=request.user,
                title=title
            )
            skill.save()
            messages.success(request,"Skill successfully added")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Sorry, something went wrong")
            return redirect(request.META.get("HTTP_REFERER"))
        
        
class SignUpView(View):
    def get(self, request):
        return render(request, 'users/signup.html')


def signup_save(request):
    if request.method != "POST": 
        return HttpResponse("Method not allowed")
    else:
        user_type = request.POST.get("user_type")
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = request.POST.get("username")


        try:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                user_type = user_type
            )
            user.save()
            messages.success(request, "Registration successfully. You can login now!")
            return redirect(request.META.get("HTTP_REFERER"))
            
        except:
            messages.error(request, "Failed to Register")
            return redirect(request.META.get("HTTP_REFERER"))