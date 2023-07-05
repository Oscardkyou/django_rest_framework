from django.db import models

class Email(models.Model):
    to = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
