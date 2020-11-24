from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


States = (
    ('Abuja', 'Abuja'),
    ('Lagos', 'Lagos'),
    ('Port Harcourt', 'Port Harcourt'),
)

# Tags = (
#
#     ('Instrumetalist','Instrumetalist'),
#     ('Musician','Musician'),
#     ('Poet','Poet'),
#     ('Rapper','Rapper'),
#     ('Dancer','Dancer'),
# )
# class Cateegory()

class User(AbstractUser):
    date_of_birth = models.DateField(null=True)
    state = models.CharField(choices=States, max_length= 20)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null= True)
    category = models.ManyToManyField('Tags')
    description = models.TextField(max_length=300,blank=True )
    cover_picture = models.ImageField(upload_to='cover_picture', null = True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pic', null= True)

    def __str__(self):
        return self.username


class Tags(models.Model):
    tag_name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.tag_name


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.FileField(upload_to='files')
    date = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tags)

    def __str__(self):
        return f'{self.user} {self.date}'

