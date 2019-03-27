from django.test import TestCase
from .models import Image,Comment, Follow, Profile,Likes

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.indian= Image()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.indian,Image))

    # Testing Save Method
    def test_save_method(self):
        self.indian.save_image()
        caption= Image.objects.all()
        self.assertTrue(len(caption) > 0)
class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.indian= Comment()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.indian,Comment))

  
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.DSC_76721.JPG= Image( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.DSC_76721.JPG,Image))

    # Testing Save Method
    
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs) 
