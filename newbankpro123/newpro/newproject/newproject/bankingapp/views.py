from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Banking


# Create your views here.
def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if username == '' or password == '':
            messages.add_message(request, messages.INFO, "Username and password are required fields")
            return redirect('/register')

        elif password != cpassword:
            messages.add_message(request, messages.INFO, "Passwords do not match")
            return redirect('/register')

        elif User.objects.filter(username=username).exists():
            messages.add_message(request, messages.INFO, "Username Taken")
            return redirect('/register')

        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            print("User created")
            return redirect('/login_view')

    return render(request, "register.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/new')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/login_view')

    return render(request, "login.html")


"""def form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        accounttype = request.POST['accounttype']
        materials = request.POST['materials']
        if User.objects.filter(username=first_name).exists():
            messages.add_message(request, messages.INFO, "name Taken")
            return redirect('/form')

        else:
            banking = Banking()
            banking.first_name = request.POST['first_name']
            banking.dob = request.POST['dob']
            banking.age = request.POST['age']
            banking.gender = request.POST['gender']
            banking.phoneno = request.POST['phoneno']
            banking.email = request.POST['email']
            banking.address = request.POST['address']
            banking.district = request.POST['district']
            banking.branch = request.POST['branch']
            banking.accounttype = request.POST['accounttype']
            banking.materials = request.POST['materials']
            banking.save()
            return render(request, "form.html")
        return render(request, "form.html")

    return render(request, "form.html")"""



 # add this line
@login_required
def form(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'] # change this line
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST.get('district')
        branch = request.POST.get('branch','')
        accounttype = request.POST.get('accounttype')
        materials = request.POST.get('materials')
        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.INFO, "Already Taken")
            return redirect('/form')

        else:
            user = User.objects.create_user(username=email, email=email)
            banking = Banking.objects.create(user=user, first_name=first_name,dob=dob,age=age,gender=gender,phoneno=phoneno, email=email,address=address,district=district,branch=branch
                                             ,accounttype=accounttype,materials=materials)
            banking.save()
            return render(request,"form.html")
        #return render(request, "form.html")

    return render(request, "form.html")






def new(request):
    return render(request, "new.html")
def logout(request):
    auth.logout(request)
    return redirect('/home')


