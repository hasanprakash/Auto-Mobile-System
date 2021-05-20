from django.urls import path
from . import views
from . import carviews

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("OTP", views.newOTP, name="OTP"),
    path("modelS", carviews.modelS, name="modelS"),
    path("finddealer", carviews.payments, name="payments"),
    path("addcomment", carviews.addcomment, name="addcomment"),
    path("customize", carviews.testing, name="testing"),
    path("logout", views.logout_session, name="logout"),
    path("ajaxcomment", carviews.ajaxcomment, name="ajaxcomment"),
    path("", views.hometest, name="hometest"),
    path("contactinfo/<str:state>", carviews.contactinfo, name="contactinfo"),
    path("info", carviews.info, name="info"),
    path("upvote", carviews.upvote, name="upvote"),
    path("seecomment", carviews.seecomment, name="seecomment"),
    path("register", views.register , name="register"),
    path("log", views.log, name="log"),
    path("end", carviews.end, name="end"),
    path("otp", views.otp, name="otp"),
    path("home", views.home1, name="home1"),
    path("temp", views.temp, name="temp"),
    path("myadmin", views.myadmin, name="myadmin"),
    path("cancellation/<int:id>", views.cancellation, name="cancellation"),
    path("cancel", views.cancel, name="cancel")
]
