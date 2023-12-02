from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from gamingApp.models import CustomUser
from .models import *
from .EmailBackEnd import EmailBackEnd

# Create your views here.
def index(request):
    games = GameModel.objects.all()
    context = {
        'game' : games
    }
    return render(request, 'index.html', context)

def signupPage(request):
    error_messages = {
        'password_error': 'Password and Confirm Password not match',
    }
    if request.method == "POST":
        uname = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        pass2 = request.POST.get("confirmpassword")

        if pass1!= pass2:
             messages.error(request, error_messages['password_error'])
        else:
            # Use your customUser model to create a user
            myuser = CustomUser.objects.create_user(username=uname, email=email, password=pass1)
            myuser.save()
            return redirect("loginPage")

    # messages.success(request, 'Signup successful.')
    return render(request, "signup.html")

def loginPage(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user!=None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('index')
            elif user_type == '2':
                return HttpResponse('This is Game Development Panel')
            elif user_type == '3':
                return HttpResponse('This is Gaming Portal Panel')
            else:
                messages.error(request, 'Email and Password are Invalid')
                return redirect('loginPage')
        else:
            messages.error(request, 'Email and Password are Invalid')
            return redirect('loginPage')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect("loginPage")


def addGame(request):
    if request.method == "POST":
        name = request.POST.get("name")
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get('image')
        gamer=GameModel(
        name=name,
        title=title,
        description=description,
        gameImage=image
        )
        gamer.save()
 
            
        # gamer = GameModel.objects.create_user(name=name, title=title, description=description)
        # gamer.title = title
        # gamer.name = name
        # gamer.description = description
        # gamer.user_type = 3  # Assuming '3' represents students

            # Save the user instance
        return redirect('index')
    return render(request, 'addGame.html')



def viewGame(request):
    return render(request, 'viewGame.html')


