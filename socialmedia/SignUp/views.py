from django.shortcuts import render,redirect
from django.http import HttpResponse
from SignUp.forms import SignUpForm ,commentForm 
from SignUp.models import SignUp ,Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.

def signup(request):
    return render(request,'SignUp.html')

def logout(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')

def comment(request):
    return render(request,'comment.html')

def sup(request):  
   
    if request.method == "POST": 
        
        form = SignUpForm(request.POST or None)  
        #return HttpResponse(form)
        
        if form.is_valid():  
            try:  
                print("Hello")
                form.save()  
                return render(request,'login.html')  
            except:  
                pass  
    else:  
        form = SignUpForm()  
    return render(request,'SignUp.html',{'form':form})  

def login_request(request):
    if request.method == "POST":    
        form = SignUpForm(request.POST)
        un = request.POST.get("username")
        ps = request.POST.get("password")
        uname = SignUp.objects.all().filter(username=un)
        
        if uname[0].username == un and uname[0].password == ps:
            return render(request,'home.html')  
            #return HttpResponse('successful')
    else:
        form = SignUpForm()
        return render(request, template_name = "login.html", context = {"form":form})

def com(request):  
   
    if request.method == "POST": 
        
        form = commentForm(request.POST or None)  
        #return HttpResponse(form)
        
        if form.is_valid():  
            try:                  

                form.save()
               # return HttpResponse('Successfull')  
                return render(request,'Showcomment.html')  
            except:  
                pass  
    else:  
        form = commentForm()  
    return render(request,'comment.html',{'form':form})