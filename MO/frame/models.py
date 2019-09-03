from django.db import models
from django.utils import timezone


# migrate:0002_auto_20190903_1505済み
# セレクトボックス、ラジオボックスで与える選択肢をテーブルで分離
class Inquiry(models.Model):

    name = models.CharField(max_length=50)
    email_address = models.EmailField(default='')
    tel_number = models.CharField(max_length=20)
    message = models.TextField()
    now_date = models.DateTimeField(default=timezone.now)


class InquirySelect(models.Model):
    def __str__(self):
        return self.inquiry_text

    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    inquiry_text = models.CharField(max_length=200)


class Reply(models.Model):
    def __str__(self):
        return self.reply_text

    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=50)
