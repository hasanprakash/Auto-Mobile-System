from home.models import Details, OrderCancelledFeedbacks
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import random

class NewForm(forms.Form):
    username = forms.CharField(max_length=40,label="" , widget=forms.TextInput(attrs={
        'class': 'inputfield',
        'placeholder': 'USERNAME',
        'id': 'rusername'
    }))
    email = forms.EmailField(max_length=100,label="", widget=forms.TextInput(attrs={
        'placeholder': 'EMAIL',
        'class': 'inputfield',
        'id': 'remail'
    }))
    password = forms.CharField(max_length=20,label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'inputfield',
        'placeholder': 'PASSWORD',
        'id': 'rpassword'
    }))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={
        'class': 'inputfield',
        'placeholder': 'USERNAME',
        'id': 'lusername'
    }))
    password = forms.CharField(max_length=20, label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'placeholder': 'PASSWORD',
        'class': 'inputfield',
        'id': 'lpassword'
    }))

class NewOTPForm(forms.Form):
    otp = forms.IntegerField(min_value=1000, max_value=9999, label="", widget=forms.TextInput(attrs={
        'placeholder': 'RECENT OTP',
        'class': 'inputfield',
        'id': 'otpfield',
    }))

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signin"))
    return render(request, "home/user2.html")
def signup(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # username = request.POST["username"]
            # email = request.POST["email"]
            # password = request.POST["password"]
        # user1 = authenticate(request, username=username, email=email, password=password)
        # user2 = authenticate(request, username=username, password=password)
            try:
                user = User.objects.get(username = username)
                return render(request, "home/index.html", {
                    "message" : "username is already exist, failed to create an account!!",
                    "form": form,
                    "form2": LoginForm()
                })
            except:
                try:
                    e = User.objects.get(email=email)
                    return render(request, "home/index.html", {
                        "message" : "email is already taken, failed to create an account!!",
                        "form": form,
                        "form2": LoginForm()
                    })
                except:
                    rand = random.randint(1000, 9999)
                    subject = "Welcome to our automobile app!"
                    message = f"Hello {username}, thank you for registering in our Web App :) \n{rand} this is your one time OTP"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email,]
                    send_mail(subject, message, email_from, recipient_list)
                    request.session['username'] = username
                    request.session['email'] = email
                    request.session['password'] = password
                    request.session['otp'] = rand
                    return render(request, "home/index.html", {
                        "message": "We have send an OTP to your mail",
                        "form1": NewOTPForm(),
                        "form2": LoginForm()
                        # "form" : form,
                        # "form1": form1
                    })

                    # User.objects.create_user(username=username, email=email, password=password)

                    # return render(request, "home/index.html", {
                    #     "message": "Now you can Sign IN!",
                    #     "form": form
                    # })
        else:
            return render(request, "home/index.html", {
                "form": form,
                "form2": LoginForm()
            })
    return render(request, "home/index.html", {
        "form": NewForm(),
        "form2": LoginForm()
    })

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # username = request.POST["username"]
            # email = request.POST["email"]
            # password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                request.session['password'] = password
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "home/index.html", {
                    "message":"invalid credintials",
                    "form2": form,
                    "form": NewForm()
                })
        else:
            return render(request, "home/index.html", {
                "message": "form is invalid",
                "form2": form,
                "form": NewForm()
            })
    return render(request, "home/index.html", {
        "form2": LoginForm(),
        "form": NewForm()
    })

def newOTP(request):
    if request.method == "POST":
        form1 = NewOTPForm(request.POST)
        if form1.is_valid():
            otp = form1.cleaned_data['OTP']
            if request.session['username'] != None and otp == request.session['otp']:
                User.objects.create_user(username=request.session['username'], email=request.session['email'], password=request.session['password'])
                return render(request, "home/index.html", {
                    "message": "OTP verified, and account created successfully!",
                    "form1": form1,
                    "form": NewForm()
                })
            else:
                return render(request, "home/index.html", {
                    "message": "Wrong OTP",
                    "form1": form1,
                    "form": NewForm()
                })
        else:
            return render(request, "home/index.html", {
                "message": "OTP invalid",
                "form1": form1,
                "form": NewForm()
            })
    else:
        return render(request, "home/index.html", {
            "form1": NewOTPForm(),
            "form": NewForm()
        })

def logout_session(request):
    logout(request)
    return HttpResponseRedirect(reverse("hometest"))


def hometest(request):
    return render(request, 'home/hometest.html',  {
        'form': NewForm(),
        'form2': LoginForm(),
        'otpform': NewOTPForm()
    })

# @csrf_exempt

def register(request):
    data = {}
    data['hasan'] = 'prakash'
    if request.is_ajax and request.method == "POST":

        form = NewForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            print(username, email, password)
            print("Received a response")
            # username = request.POST["username"]
            # email = request.POST["email"]
            # password = request.POST["password"]
            # user1 = authenticate(request, username=username, email=email, password=password)
            # user2 = authenticate(request, username=username, password=password)
            try:
                user = User.objects.get(username = username)
                data['iserror'] = 'true'
                return JsonResponse(data)
                # return render(request, "home/index.html", {
                #     "message" : "username is already exist, failed to create an account!!",
                #     "form": form,
                #     "form2": LoginForm()
                # })
            except:
                try:
                    e = User.objects.get(email=email)
                    data['iserror'] = 'true'
                    return JsonResponse(data)
                    # return render(request, "home/index.html", {
                    #     "message" : "email is already taken, failed to create an account!!",
                    #     "form": form,
                    #     "form2": LoginForm()
                    # })
                except:
                    rand = random.randint(1000, 9999)
                    subject = "Welcome to our automobile app!"
                    message = f"Hello {username}, thank you for registering in our Web App :) \n{rand} this is your one time OTP"
                    email_from = settings.EMAIL_HOST_USER
                    # recipient_list = [email,]
                    # send_mail(subject, message, email_from, recipient_list)
                    send_mail(subject, message, email_from, [email], fail_silently=False)
                    request.session['username'] = username
                    request.session['email'] = email
                    request.session['password'] = password
                    request.session['otp'] = rand
                    data['iserror'] = 'false'
                    return JsonResponse(data)
                    # return render(request, "home/index.html", {
                    #     "message": "We have send an OTP to your mail",
                    #     "form1": NewOTPForm(),
                    #     "form2": LoginForm()
                    #     # "form" : form,
                    #     # "form1": form1
                    # })
        else:
            data['iserror'] = 'true'
            return JsonResponse(data)
            # return render(request, "home/index.html", {
            #     "form": form,
            #     "form2": LoginForm()
            # })
    else:
        return JsonResponse({"error": ""}, status=400)

def log(request):
    data = {}
    data['hasan'] = 'prakash'
    if request.is_ajax and request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                request.session['password'] = password

                data['iserror'] = 'false'
                return JsonResponse(data)
            else:
                data['iserror'] = 'true'
                return JsonResponse(data)
        else:
            data['iserror'] = 'true'
            print("Form is not validated")
            return JsonResponse(data)
    else:
        return JsonResponse({"error": ""}, status=400)

def otp(request):
    data = {}
    data['hasan'] = 'prakash'
    if request.is_ajax and request.method == "POST":
        form = NewOTPForm(request.POST)
        if form.is_valid():
            otp = request.POST['otp']
            # print(request.session['username'], otp, request.session['otp'], request.session['username'] != None, str(otp) == str(request.session['otp']))
            if request.session['username'] != None and str(otp) == str(request.session['otp']):
                User.objects.create_user(username=request.session['username'], email=request.session['email'], password=request.session['password'])
                data['iserror'] = 'false'
                return JsonResponse(data)
            else:
                data['iserror'] = 'true'
                return JsonResponse(data)
        else:
            data['iserror'] = 'true'
            print("form is invalid")
            return JsonResponse(data)
    else:
        return JsonResponse({"error": ""}, status=400)

@login_required(login_url='/home')
def home1(request):
    try:
        print(request.session['username'])
    except:
        return HttpResponseRedirect(reverse("hometest"))
    return render(request, "home/home1.html", {
        'user': request.session['username']
    })

def temp(request):
    return render(request, "home/temporary.html")


def myadmin(request):
    return render(request, "home/myadmin.html")


@login_required(login_url='/home')
def cancellation(request, id):
    return render(request, "home/cancellation.html", {
        'id': id
    })


@login_required(login_url='/home')
def cancel(request):
    if request.method == "POST":
        feedback = request.POST['feedback']
        orderid = request.POST['orderid']
        boolean_field = Details.objects.filter(id=orderid)[0]
        boolean_field.ordercancelled = not boolean_field.ordercancelled
        boolean_field.save()
        OrderCancelledFeedbacks.objects.create(orderid=orderid, username=boolean_field.username, feedback=feedback)

        return render(request, "home/home1.html", {
            'hasanprakash':'Your Order is Cancelled Successfully..'
        })
    return render(request, "home/home1.html", {
        'hasanprakash': 'Order Cancellation Failed..'
    })