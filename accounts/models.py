from main.models import Plan
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField, OneToOneField

# Create your models here.
class userprofile(models.Model):
    user = OneToOneField(User, related_name='Profile', on_delete=models.CASCADE)
    BitcoinWallet = models.TextField()
    SecretQuestion = models.TextField()
    SecretAnswer = models.TextField()


    def __str__(self):
        return self.user


class Investments(models.Model):
    user = models.ForeignKey(User, related_name='investments', on_delete=models.DO_NOTHING)
    plan = models.ForeignKey(Plan, related_name='investments', on_delete=models.DO_NOTHING)
    deposit = models.DecimalField(max_digits=11, decimal_places=2)
    amountreturn = models.DecimalField(max_digits=11, decimal_places=2)
    btcdeposit = models.FloatField(max_length=20)
    btcreturn = models.FloatField(max_length=20)
    status = models.CharField(max_length=50)
    

    def __str__(self) :
        return self.user.username