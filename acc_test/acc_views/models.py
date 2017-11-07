from django.db import models
from django.core.urlresolvers import reverse


class Users(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=60)
    registration_date = models.DateTimeField(auto_now=True)
    email_address = models.CharField(max_length=300)
    user_picture = models.FileField(null=True, blank=True)



    def get_absolute_url(self):
        return reverse('acc_views:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.first_name + " " + self.last_name


    #def __unicode__(self):
     #   return self.first_name




class Accounts(models.Model):
    is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(Users)
    type = models.CharField(max_length=10)
    acc_description = models.CharField(max_length=1500)
    balance = models.IntegerField()
    credit = models.IntegerField()
    debit = models.IntegerField()


    def __str__(self):
        return "User id: {},User Name: {}, Balance {}".format(self.user_id_id, self.user_id, self.balance)

















# Create your models here.
