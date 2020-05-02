from django.shortcuts import render,redirect    
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from authentication.forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})
@login_required
def logoutView(request):
    logout(request)
    return redirect('/')

def registerView(request):
    if request.method=="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})

