from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User


# Create your views here.

def register(request):
    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        if password == confirmPassword:
            if User.objects.filter(username=userName).exists():
                messages.info(request, 'Username already Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Registered')
                return redirect('register')

            else:
                userDetails = User.objects.create_user(
                    first_name=firstName,
                    last_name=lastName,
                    username=userName,
                    email=email,
                    password=password
                )

                userDetails.save()
                return redirect('/')
        else:
            messages.info(request, 'wrong password')
            return redirect('register')

    else:
        return render(request, 'register.html')
