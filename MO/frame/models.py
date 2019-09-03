from django.db import models
from django.utils import timezone


# migrate済み
class InquiryInfo(models.Model):

    name = models.CharField(max_length=50)
    email_address = models.EmailField(default='')
    tel_number = models.CharField(max_length=20)
    inquiry_data = models.CharField(max_length=200, unique=True)
    reply = models.CharField(max_length=20, unique=True)
    message = models.TextField()
    now_date = models.DateTimeField(default=timezone.now)
