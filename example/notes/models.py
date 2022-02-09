from django.db import models

class Notes(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return f"{ self.content } { self.created }"


       
