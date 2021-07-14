from django.db import models

# Create your models here.
class System(models.Model):
    runningdays = models.CharField(max_length=10)
    totalinvestments = models.DecimalField(max_digits=11, decimal_places=2)
    revenupaid = models.DecimalField(max_digits=11, decimal_places=2)


    def __str__(self) :
        return self.id


class Plan(models.Model):
    planname = models.CharField(max_length=10)
    dividend = models.DecimalField(max_digits=11, decimal_places=2)
    roi = models.IntegerField()
    min_deposit = models.IntegerField()
    max_deposit = models.IntegerField()
    plan_image = models.FileField(upload_to='plans')

    def __str__(self) :
        return self.planname



class Rating(models.Model):
    commentby = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    review = models.CharField(max_length=255)
    rating = models.IntegerField()
    commend_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title



