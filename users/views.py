from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.

def registerUser(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            # print("valid form")
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"{username} registered successfully")
            return redirect('login',{'messages':messages})
    form=RegisterForm()
    return render(request,'users/register-user.html',{'form':form})

@login_required
def userProfile(request):
    return render(request,'users/profile.html')

