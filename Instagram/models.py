from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio= models.CharField(max_length=100)
    prof_pic= CloudinaryField('image')
    following= models.ManyToManyField(User, related_name='follower', blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()

    def profiles_posts(self):
        return self.image_set.all()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    class Meta:
        ordering=('-created',)

