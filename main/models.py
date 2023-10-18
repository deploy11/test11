from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    body =  RichTextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ('-id',)

class ProductImage(models.Model):
    product = models.ForeignKey(Blog, on_delete=models.CASCADE)    
    image = CloudinaryField()

class Teachers(models.Model):
    name = models.CharField(max_length=500)
    uneversitiy = models.CharField(max_length=500)
    yosh = models.CharField(max_length=500)
    tel = models.CharField(max_length=500)
    telegram_username = models.CharField(max_length=500)
    more = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

class sinf(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

class Comment(models.Model):
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE,verbose_name='o`qtuvchini tanlang')
    student_name = models.CharField(max_length=500,verbose_name='ismingiz')
    student_class = models.ForeignKey(sinf,on_delete=models.CASCADE,verbose_name='sinfingiz')
    body = models.TextField(verbose_name='savolingiz')

    def __str__(self):
        return self.student_name

class Javob(models.Model):
    comments = models.IntegerField()
    names = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.names

class Books(models.Model):
    name = models.CharField(max_length=500)
    image = CloudinaryField()
    book_class = models.CharField(max_length=500)
    more = models.TextField()
    audio = models.FileField(upload_to='audios/')
    file = models.FileField(upload_to='files/')