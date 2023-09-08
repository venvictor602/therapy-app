from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['contact_date']


    def __str__(self):
        return self.name