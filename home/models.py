from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comments(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    storename = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)
    cmt = models.TextField(max_length=1513)
    response = models.CharField(max_length=10)
    votes = models.IntegerField()
    upvote = models.ManyToManyField(User, related_name="upvoting", blank=True)
    downvote = models.ManyToManyField(User, related_name="downvoting", blank=True)
    def __str__(self):
        return f"{self.user}'s comment for store {self.storename}"



class Details(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    carcolor = models.CharField(max_length=20)
    detailcolor = models.CharField(max_length=20)
    interiorcolor = models.CharField(max_length=20)
    enginetype = models.CharField(max_length=30)
    rim = models.CharField(max_length=20)
    spoiler = models.CharField(max_length=20)
    storename = models.CharField(max_length=20)
    ordercancelled = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.username}"

class OrderCancelledFeedbacks(models.Model):
    orderid = models.IntegerField()
    username = models.CharField(max_length=50)
    feedback = models.TextField(max_length=1513)
    def __str__(self):
        return F"{self.username}"
