from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from App_Login.forms import ProfilePicForm, RegisterForm, UserProfileChangeForm

# Create your views here.


def register(request):
    form = RegisterForm()
    registered = False

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dicts = {'form': form, 'registered': registered}
    return render(request, 'App_Login/register.html', context=dicts)


def login_page(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    return render(request, 'App_Login/login.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={})


@login_required
def user_change(request):
    current_user = request.user
    form = UserProfileChangeForm(instance=current_user)
    changed = False

    if request.method == 'POST':
        form = UserProfileChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChangeForm(instance=current_user)
            changed = True
    return render(request, 'App_Login/change_profile.html', context={'form': form, 'changed':changed})


@login_required
def change_pass(request):
    current_user = request.user
    form = PasswordChangeForm(current_user)
    changed = False

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user= current_user)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'App_Login/change_pass.html', context={'form': form, 'changed':changed})

@login_required
def add_pro_pic(request):
    form = ProfilePicForm()

    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES)
        if form.is_valid():
            user_object = form.save(commit=False)
            user_object.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))

    return render(request, 'App_Login/add_pro_pic.html', context={'form': form})

def change_pro_pic(request):
    form = ProfilePicForm(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePicForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/add_pro_pic.html', context={'form':form})