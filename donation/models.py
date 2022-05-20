from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

MODE_CHOICE = (
    ("Cash","Cash"),
    ("Cheque","Cheque"),
    ("Draft","Draft"),
)

class Donation(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10,blank=True,null=True)

    date_donation = models.DateTimeField(auto_now_add=True)

    mode_donation = models.CharField(max_length=10,choices=MODE_CHOICE,default='Cash')

    amount = models.IntegerField(null=True,blank=True)

    cheque_no = models.CharField(max_length=6,null=True,blank=True)
    cheque_micr = models.CharField(max_length=9,null=True,blank=True)
    cheque_date = models.DateField(null=True,blank=True)
    cheque_amount = models.IntegerField(null=True,blank=True)


    draft_no = models.CharField(max_length=6,null=True,blank=True)
    draft_micr = models.CharField(max_length=9,null=True,blank=True)
    draft_date = models.DateField(null=True,blank=True)
    draft_amount = models.IntegerField(null=True,blank=True)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('article_detail', args=(str(self.id)))
        return reverse('receipt-main')


