from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login,logout




User = get_user_model()
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def causes(request):
    return render(request,"causes.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")

def loginform(request):
    if request.method!="POST":
        return render(request,"login-form.html")
    else:
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(username=email,password=password)

        if user:
            login(request,user)
            return render(request,'index.html')
        else:
            return render(request,'login-form.html',{'message':'email id or password incoreect'})


def registerform(request):
    if request.method=='POST':
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        email=request.POST.get('email')
        username=request.POST.get('username')

        if (password==confirm_password):
            try:
                match = User.objects.get(email=email)
                return render(request,"register-form.html",{'massage:email already taken'})

            except User.DoesNotExist:
                 User.objects.create_user(username=email,email=email,password=password)
                 user= authenticate(username=email,password=password)
                 loginform(request)
                 return render(request,'index.html')
        else:
                return render(request,"register-form.html",{'massage:mismatch password'})
    else:
        return render(request,"register-form.html")
   
def forgotpswdform(request):
    return render(request,"forgot-pswd-form.html")

def logoutform(request):
    logout(request)
    return redirect(index)


  