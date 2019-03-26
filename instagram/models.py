from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = "images/",null = True)
    user = models.ForeignKey(User,null=True)
    image_name = models.CharField(max_length = 30,null = True)
    
    image_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    
    


    def __str__(self):
    	return self.image_name

    def delete_image(self):
    	self.delete()

    def save_image(self):
    	self.save()

    def update_caption(self,new_caption):
    	self.image_caption = new_caption
    	self.save()

	# @classmethod
    # def all_images(cls):
    #     images = cls.objects.all()
    #     return images 

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image

    # @classmethod
    # def get_images_by_user(cls,id):
    #     sent_imgaes = Image.objects.filter(user_id=id)
    #     return sent_images

    # @classmethod
    # def get_images_by_id(cls,id):
    #     fetched_image = Image.objects.get(id = id)
    #     return  fetched_image

    class Meta:
    	ordering = ['-pub_date']


    

    def save_profile(self):
    	self.save()

class Profile(models.Model):
	username = models.CharField(default='User',max_length=30)
	profile_image = models.ImageField(upload_to = "profile/",null=True)
	bio = models.TextField(default='',blank = True)
	# first_name = models.CharField(max_length =30)
	# last_name = models.CharField(max_length =30)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

	@classmethod
	def search_by_name(cls,search_term):
		photos = cls.objects.filter(name__icontains = search_term)
		return photos

class Comment(models.Model):
	user = models.ForeignKey(User, null= True)
	image = models.ForeignKey(Image, null= True,related_name='comment')
	comment= models.TextField( blank=True)
	
	def __str__(self):
		return self.comment


	def delete_comment(self):
		self.delete()

	def save_comment(self):
		self.save()


class Likes(models.Model):
	user = models.ForeignKey(Profile,null=True)
	# pic = models.ForeignKey(Pic,null=True)

	def __int__(self):
		return self.name

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save() 

















