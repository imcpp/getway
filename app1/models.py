from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=64)
    course_price=models.FloatField()
    teacher=models.CharField(max_length=64)
    image=models.ImageField(upload_to='image')
    about=models.TextField()
    starting_date=models.DateField()
    video=models.FileField(null=True,blank=True,upload_to='video')
