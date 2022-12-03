from django.db import models


class SentimentsData(models.Model):
    input_txt = models.TextField()
    remarks = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

