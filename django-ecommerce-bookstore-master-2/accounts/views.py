from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['Enrollment']
        password1 = request.POST['Password']
        password2 = request.POST['Password2']
        first_name = request.POST['First Name']
      
       

        
        if User.objects.filter(username=username).exists():
              messages.info(request, 'User already exists')
              return redirect('signup')
        
        
        
        if password1 == password2:
                   user = User.objects.create_user(username=username, password=password1, first_name=first_name)
                   user.save();
                   messages.info(request, 'Account succesfully created')
                   return redirect('signup')
                   
        else:
                   messages.info(request, 'Password entered is not same')
                   return redirect('signup')
        
     
    else:
        return render(request, 'signup1.html')

def login(request):
    if request.method =='POST':
          username = request.POST['Enrollment']
          password = request.POST['Password']    

          user= auth.authenticate(username=username, password=password)

          if user is not None:
                auth.login(request, user)
                return redirect('/')
          else:
                messages.info(request, 'Credentials Invalid')
                return redirect('login')
          
    else:
          return render(request, 'login.html')
    

def logout(request):
      auth.logout(request)
      return redirect('/')