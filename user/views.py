from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistration, LoginForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            messages.success(request, "Thanks " + nm + "..! For Joining Our Portal..!!")
            fm = UserRegistration()
    else:
        fm = UserRegistration()
    user = User.objects.all()
    return render(request, 'user/register.html', {'form': fm, 'user': user})    

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('/dashboard')  # Redirect to the dashboard after login
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})