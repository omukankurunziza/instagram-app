from django.db import models
import datetime as dt
# from django.contrib.auth.models import User
# from tinymce.models import HTMLField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_user(self):
        self.save() 

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'pictures/')
    bio = models.CharField(max_length =70)
   
    def __str__(self):
        return self.name
        
    def save_profile(self):
        self.save()    

    def delete_profile(self):
        Profile.objects.filter(id = self.pk).delete()
   
    def update_profile(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)  

class Image(models.Model):

    image =image = models.ImageField(upload_to = 'pictures/')
    image_name = models.CharField(max_length =60)
    image_caption = models.CharField(max_length =60)
    profile = models.ForeignKey(Profile)
    tags = models.ManyToManyField(tags)
    like =  models.TextField()
    comments =  models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
    def save_image(self):
        self.save()    

    def delete_image(self):
        Image.objects.filter(id = self.pk).delete()
   
    def update_image_caption(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)  
    
    
#     @classmethod
#     def todays_news(cls):
#             today = dt.date.today()
#             news = cls.objects.filter(pub_date__date = today)
#             return news

#     @classmethod
#     def days_news(cls,date):
#             news = cls.objects.filter(pub_date__date = date)
#             return news

#     @classmethod
#     def search_by_title(cls,search_term):
#             news = cls.objects.filter(title__icontains=search_term)
#             return news

# class NewsLetterRecipients(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.EmailField()
