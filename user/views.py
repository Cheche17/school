from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.utils.text import slugify


from .models import UserAccount, UserManager

def signup(request):
    if request.method == 'POST':
         
         form = CustomUserForm(request.POST)
        
         if form.is_valid():
               user = form.save()
               login(request, user)
               
               messages.success(request, "Registration successful." )
               return redirect('account') 
          
    else:
         form = CustomUserForm()  
        
    return render(request, '', {
         'form': form
    })
    
def signin(request):
     if request.method == 'POST':
          
          form = AuthenticationForm(request.POST, data=request.POST)
          
          if form.is_valid():
               
               email = form.cleaned_data.get('email')
               password = form.cleaned_data.get('password')
               user = authenticate(email=email, password=password)
               
               if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {email}.")
                    return redirect(request, "")
               
          else:
               messages.error(request,"Invalid username or password.")
     else:
          form = AuthenticationForm()
               
     return render(request, '', {
         'form': form
    })