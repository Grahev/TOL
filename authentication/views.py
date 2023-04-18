from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView    

# Create your views here.

class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('tracker:project_list') 

def logout_view(request):
        logout(request)
        return redirect('authenticator:login')
    