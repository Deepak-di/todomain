from django.db import models

# Create your models here.

class ToDo(models.Model):
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    user=models.CharField(max_length=200)
    options={
        {"pending","pending"},
        {"completed","completed"}
    }
    status=models.CharField(max_length=200,choices=options,default="pending")


    def __str__(self):
        return self.title
