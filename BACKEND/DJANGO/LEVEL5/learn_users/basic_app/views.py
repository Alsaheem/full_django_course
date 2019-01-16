from django.shortcuts import render
from basic_app.forms import userForm,userprofileinfoform

#######
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registered=False

    if request.method== 'POST':
        user_form = userForm(data=request.POST)
        profile_form = userprofileinfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) # this hashes the password with our hashing algorithm
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = userForm()
        profile_form = userprofileinfoform()


    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT IS NOT ACTIVE')
        else:
            print('someont tried to login and failed')
            print('username: {} and password : {}'.format(username,password))

            return HttpResponse('invalid login details , please review!!! ')

    else:
        return render(request,'basic_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('you are logged in successfully')
