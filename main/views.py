from django.shortcuts import render
from django.views import View


# Create your views here.
class IndexView(View):
    def get(self, request):

        return render(request, 'pages/index.html')
    
class LoginView(View):
    def get(self, request):

        return render(request, 'pages/login.html')
    
class SignupView(View):
    def get(self, request):

        return render(request, 'pages/signup.html')