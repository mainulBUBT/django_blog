from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponsePermanentRedirect
from django.urls import reverse

# Create your views here.

def register(request):
    form = UserCreationForm()
    registered = False

    if request.method == 'POST':
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            registered = True
    
    dicts = {'form': form, 'registered': registered}
    return render(request, 'App_Login/register.html', context=dicts)

def login_page(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.changed_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
                
    return render(request, 'App_Login/login.html', context={'form': form})