from django.shortcuts import render
from django import forms
# from .models import S0, S1, S2, S3, S4
from .models import Comments, Details
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
from collections import defaultdict
from django.db.models import Max
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
import datetime;

class PaymentForm(forms.Form):
    firstName = forms.CharField(max_length=20, label="FirstName")
    lastName = forms.CharField(max_length=20, label="LastName")
    email = forms.EmailField(max_length=50, label="Email")
    phoneNumber = forms.IntegerField(max_value=15, label="PhoneNumber")

class CardForm(forms.Form):
    name = forms.CharField(max_length=45, label="Name of the Card Holder")
    number = forms.CharField(max_length=20, label="Card Number")
    expireMonth = forms.IntegerField(min_value=1, max_value=12, label="Expiration Month")
    expireYear = forms.IntegerField(min_value=2021, max_value=2100, label="Expiration Year")
    cvv = forms.IntegerField(min_value=100, max_value=999, label="CVV")
    zipcode = forms.IntegerField(min_value=100000, max_value=999999, label="ZIP Code")

class CommentForm(forms.Form):
    # cmt = forms.CharField(widget=forms.Textarea)
    # cmt = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'inputfield'}))
    cmt = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'inputfield', 'rows': 1, 'id': 'cmt'}), label='')


def modelS(request):
    return render(request, "home/buymodels.html", {
        "cashprice":5713881,
        "leaseprice":72715,
        "loanprice":78611,
        "paymentform":PaymentForm(),
        "cardform": CardForm()
    })

def payments(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("hometest"))
    else:
        try:
            use = request.session['username']
            pas = request.session['password']
        except:
            print("error error error high alert")
            return HttpResponseRedirect(reverse("hometest"))
    return render(request, "home/dealer1.html", {
        "matter": "Enter your comment here",
        "cmtform": CommentForm(),
        # "S0" : S0.objects.all()[::-1],
        # "S1" : S1.objects.all()[::-1],
        # "S2" : S2.objects.all()[::-1],
        # "S3" : S3.objects.all()[::-1],
        # "S4" : S4.objects.all()[::-1]
    })


def comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            cmt = form.cleaned_data['cmt']
            lifesaver = request.POST['lifesaver']
            try:
                if request.session['username'] == None:
                    return HttpResponseRedirect(reverse("hometest"))
            except:
                return HttpResponseRedirect(reverse("hometest"))
            # S3(lifesaver.upper()).objects.create(cmt = cmt)
            if lifesaver == "s0":
                S0.objects.create(user=request.session['username'], s0 = cmt)
            elif lifesaver == "s1":
                S1.objects.create(user=request.session['username'], s1 = cmt)
            elif lifesaver == "s2":
                S2.objects.create(user=request.session['username'], s2 = cmt)
            elif lifesaver == "s3":
                S3.objects.create(user=request.session['username'], s3 = cmt)
            elif lifesaver == "s4":
                S4.objects.create(user=request.session['username'], s4=cmt)
            return HttpResponseRedirect(reverse("payments"))
            # return render(request, "home/dealer1.html", {
            #     "message": "Success",
            #     "cmtform": CommentForm()
            # })
        else:
            return render(request, "home/dealer1.html", {
                "message": "form invalid",
                "cmtform": CommentForm(request.POST)
            })
    else:
        return render(request, "home/dealer1.html", {
            "message": "form invalid",
            "cmtform": CommentForm()
        })

def ajaxcomment(request):
    data = {}
    if request.is_ajax and request.method == "POST":
        form = CommentForm(request.POST)
        print(request.POST['cmt'])
        cmt = request.POST['cmt']
        lifesaver = request.POST['lifesaver']
        if form.is_valid():
            # form.save()
            data['username'] = request.session['username']
            data['cmt'] = cmt
            try:
                if request.session['username'] == None:
                    return HttpResponseRedirect(reverse("hometest"))
            except:
                return HttpResponseRedirect(reverse("hometest"))
            if lifesaver == "s0":
                S0.objects.create(user=request.session['username'], s0 = cmt)
                data['date'] = S0.objects.last().date
            elif lifesaver == "s1":
                S1.objects.create(user=request.session['username'], s1 = cmt)
                data['date'] = S1.objects.last().date
            elif lifesaver == "s2":
                S2.objects.create(user=request.session['username'], s2 = cmt)
                data['date'] = S2.objects.last().date
            elif lifesaver == "s3":
                S3.objects.create(user=request.session['username'], s3 = cmt)
                data['date'] = S3.objects.last().date
            elif lifesaver == "s4":
                S4.objects.create(user=request.session['username'], s4 = cmt)
                data['date'] = S4.objects.last().date
            # print(S3.objects.last().date)
            # serialize in new friend object in json
            # ser_instance = serializers.serialize('json', [ instance, ])
            # send to client side.
            # return JsonResponse({"instance": ser_instance}, status=200)
            return JsonResponse(data)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)

@login_required(login_url='/home')
def testing(request):
    try:
        print(request.session['username'])
    except:
        return HttpResponseRedirect(reverse("hometest"))
    try:
        print(request.session['storename'])
        request.session['gotocustomize'] = True
    except:
        return HttpResponseRedirect(reverse("payments"))
    try:
        if request.session['storename'] == None or request.session['gotocustomize'] != True:
            return HttpResponseRedirect(reverse("finddealer"))
    except:
        return HttpResponseRedirect(reverse("payments"))
    if request.method == "POST":
        brand = request.POST['brand']
        model = request.POST['model']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        country = request.POST['country']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']


        request.session['brand'] = brand
        request.session['model'] = model
        request.session['firstname'] = firstname
        request.session['lastname'] = lastname
        request.session['address'] = address
        request.session['country'] = country
        request.session['city'] = city
        request.session['phone'] = phone
        return render(request, "home/testing.html")

    else:
        return HttpResponseRedirect(reverse("payments"))
    return render(request, "home/testing.html")

@login_required(login_url='/home')
def contactinfo(request, state):
    try:
        print(request.session['username'])
    except:
        return HttpResponseRedirect(reverse("hometest"))

    if state == "showroomD":
        name = "Hoysala AutoMotives Pvt Ltd"
        city = "Banglore"
        street = "Lavelle Road"
        address = "10/8, Umiya Landmark, Ground Floor"
        pincode = 560001
        phone = "+ 91 994 563 3900"
    elif state == "showroomE":
        name = "Infinity Cars Pvt Ltd"
        city = "Hyderabad"
        street = "Passport Office, Veer Savarkar Road, Prabhadevi"
        address = "Unit No.1, Ground Floor, Aman Chambers, Opposite New"
        pincode = 500008
        phone = "(+91) 9930221961"
    elif state == "showroomA":
        name = "Delhi Showroom"
        city = "New Delhi"
        street = "Moti Nagar, Crossing"
        address = "69, Unit-2, TSG Complex, 1-A, Najafgarh Rd"
        pincode = "110015"
        phone = "96431 01006"
    elif state == "showroomB":
        name = "Kolkata AutoMobile Showroom"
        city = "Kolkata"
        street = "Lake Town"
        address = "VIP Rd, Sreebhumi"
        pincode = "700048"
        phone = "89294 00461"
    elif state == "showroomC":
        name = "Chennai Car Bazaar"
        city = "Chennai"
        street = "Panchanna Pally, Topsia"
        address = "235 E, panchanagram, Eastern Metropolitan Bypass, opp sanjha chulha restaurant"
        pincode = "700100"
        phone = "93311 16991"

    request.session['storename'] = state

    return render(request, "home/contactinfo.html", {
        'state': state,
        'name': name,
        'city': city,
        'street': street,
        'address': address,
        'pincode': pincode,
        'phone': phone
    })

def info(request):


    return render(request, "home/success.html", {
    })

def upvote(request):
    data = {}
    if request.is_ajax:
        isupvoted = request.POST['isupvoted']
        isdownvoted = request.POST['isdownvoted']
        commentid = request.POST['commentid']
        votes = request.POST['votes']
        votechange = request.POST['votechange']
        print(isupvoted, isdownvoted)
        try:
            if request.session['username'] == None:
                return HttpResponseRedirect(reverse("hometest"))
        except:
            return HttpResponseRedirect(reverse("hometest"))
        username = request.session['username']

        accountuser = User.objects.filter(username=username)[0]
        responsetoadd = Comments.objects.filter(id=commentid)[0]

        if isupvoted=="true" and isdownvoted=="false":
            responsetoadd.upvote.add(accountuser)
            responsetoadd.downvote.remove(accountuser)
            print("UPVOTED")
        elif isupvoted == "false" and isdownvoted == "true":
            responsetoadd.downvote.add(accountuser)
            responsetoadd.upvote.remove(accountuser)
            print("DOWNVOTED")
        else:
            responsetoadd.upvote.remove(accountuser)
            responsetoadd.downvote.remove(accountuser)
        print(responsetoadd.votes,"changes to", votes)
        # responsetoadd.votes = str(int(responsetoadd.votes)+int(votechange))
        responsetoadd.votes = responsetoadd.upvote.all().count() - responsetoadd.downvote.all().count()
        responsetoadd.save()


        return JsonResponse(data)

    return JsonResponse({"error": ""}, status=400)

def seecomment(request):
    data = {}
    data['hasan'] = "prakash"
    if request.is_ajax:
        storename = request.POST['storename']
        obj = Comments.objects.filter(storename=storename)
        data['obj'] = list(obj.values_list('user_id__username', 'date', 'cmt', 'votes', 'response', 'id'))
        # print("obj.values() = ", obj.values())
        # print("obj.values_list() = ", obj.values_list())
        # print(obj.values_list()[0])
        # print(obj[0].user)
        print(data['obj'][0][1].year, data['obj'][0][1].hour)

        username = request.session['username']
        data['upvoting'] = list(User.objects.filter(username=username)[0].upvoting.all().values_list('id'))
        data['downvoting'] = list(User.objects.filter(username=username)[0].downvoting.all().values_list('id'))
        d1 = defaultdict(lambda:"hasan")
        d2 = defaultdict(lambda:"hasan")
        for i in data['upvoting']:
            d1[i[0]] = 1
        for i in data['downvoting']:
            d2[i[0]] = 1
        data['upvote'] = d1
        data['downvote'] = d2
        data['timenow'] = datetime.datetime.now()
        data['year'] = data['timenow'].year
        data['month'] = data['timenow'].month
        data['day'] = data['timenow'].day
        data['hour'] = data['timenow'].hour
        data['minute'] = data['timenow'].minute
        data['second'] = data['timenow'].second
        data['count'] = obj.count()
        # max_rating = Comments.objects.aggregate(Max('votes'))['votes__max']
        l = list(obj.values_list('votes'))
        if l == []:
            max_rating = 0
            data['maxvalue'] = None
            return JsonResponse(data)
        else:
            max_rating = max(l)[0]
            data['maxvalue'] = Comments.objects.filter(votes=max_rating, storename=storename).values_list('user_id__username', 'votes', 'cmt', 'id')[0]
            print(data['maxvalue'])
        # data['maxvalue'] = Comments.objects.filter(votes=max_rating).values_list('user_id__username', 'votes', 'cmt', 'id')[0]
        return JsonResponse(data)
    return JsonResponse({"error" : ""}, status=400)

def addcomment(request):
    data = {}
    data['hasan'] = "prakash"
    if request.is_ajax:
        user = request.session['username']
        storename = request.POST['storename']
        cmt = request.POST['cmt']
        votes = request.POST['votes']
        print(request.session['username'], storename)
        print(cmt)
        print(votes)
        Comments.objects.create(user=User.objects.filter(username=user)[0], storename=storename, cmt=cmt, response="None", votes=votes)
        obj = Comments.objects.last()
        data['user'] = user
        data['date'] = obj.date
        data['cmt'] = cmt
        data['votes'] = votes
        data['id']= obj.id
        return JsonResponse(data)
    return JsonResponse({"error": ""}, status=400)

def end(request):
    data = {}
    data['hasan']='prakash'
    if request.is_ajax:
        cc = request.POST['cc']
        dc = request.POST['dc']
        ic = request.POST['ic']
        et = request.POST['et']
        r = request.POST['r']
        s = request.POST['s']
        finalcost = request.POST['finalcost']
        print(cc, dc, ic, et, r, s, finalcost)
        username = request.session['username']
        firstname = request.session['firstname']
        lastname = request.session['lastname']
        city = request.session['city']
        address = request.session['address']
        phone = request.session['phone']
        storename = request.session['storename']


        Details.objects.create(username=username, firstname=firstname, lastname=lastname, city=city, address=address, phone=phone, carcolor=cc, detailcolor=dc, interiorcolor=ic, enginetype=et, rim=r, spoiler=s, storename=storename)
        # email_from = settings.EMAIL_HOST_USER
        # email = request.session['email'] = User.objects.filter(username=request.session['username'])[0].email
        # print(email)
        # recipient_list = [email,]
        # html_content = "<p><a href={% url 'cancellation' %}>click here</a> to cancel your order</p>"
        # msg = EmailMultiAlternatives(subject, message, email_from, recipient_list)
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()


        subject = "Request Accepted.."
        email_from = settings.EMAIL_HOST_USER
        email = request.session['email'] = User.objects.filter(username=request.session['username'])[0].email
        recipient_list = [email,]
        html_content = f"""<div style="font-family:sans-serif; color:black;">Your order request is successfully reached to us. Your car will be reached to {request.session['storename']} within 6 months. We will let you know about your order status regularly. If you have any questions or if you want to know about your order don't forget to take our services by contacting us. Please ensure the details we have taken from you so far about your order.<br>
            Username       - {username}<br>
            First Name     - {firstname}<br>
            Last Name      - {lastname}<br>
            Country        - {request.session['country']}<br>
            City           - {city}<br>
            Address        - {address}<br>
            Phone          - {phone}<br>
            Brand          - {request.session['brand']}<br>
            Model          - {request.session['model']}<br>
            Color          - {cc}<br>
            Details Color  - {dc}<br>
            Interior Color - {ic}<br>
            Engine Model   - {et}<br>
            Rim type       - {r}<br>
            Spoiler type   - {s}<br>
            Final Cost     - {finalcost[0]+","+finalcost[1:3]+","+finalcost[3:5]+","+finalcost[5:]} /-<br>
            Showroom Name  - {storename}<br>

        <p><a href="http://{request.META['HTTP_HOST']}/home/cancellation/{Details.objects.last().id}">click here</a> to cancel your order</p></div>"""
        print(request.META['HTTP_HOST'])
        msg = EmailMessage(subject, html_content, email_from, recipient_list)
        msg.content_subtype = "html"  # Main content is now text/html
        msg.send()





        # send_mail(subject, message, email_from, recipient_list)


        return JsonResponse(data)
    return JsonResponse({"error": ""}, status=400)