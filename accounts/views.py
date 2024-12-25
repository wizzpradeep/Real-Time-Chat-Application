from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class Home(View):

    def get(self,request):
        context = {}
        return render(request, 'home.html', context)

    def get(self,request):
        context = {}
        return render(request, 'home.html', context)



class Signup(View):

    def get(self,request):

        form  = UserCreationForm()
        context = {
            'form':form
        }
        return render(request, 'signup.html', context)

    def post(self,request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        context = {
            'form':form
        }
        return render(request, 'signup.html', context)



class Signin(View):

    def get(self,request):

        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'signin.html', context)

    def post(self,request):

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        context = {
            'form':form
        }
        return render(request, 'signin.html', context)

def log_out(request):
    logout(request)
    return redirect('signin')