from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
# Create your models here.
 
   

class Location(models.Model):
    location_name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.location_name
 
    
class Cartegory(models.Model):
    cartegory_name = models.CharField(max_length=30)
  
    def search_by_category(cls,search_photo):
         photo=cls.objects.filter(category = search_photo)
         return photo  
    
    def __str__(self):
        return self.cartegory_name
     
class Photo(models.Model):
     image = CloudinaryField('image')
     image_name=models.CharField(max_length=30)
     image_description = models.TextField()
     upload_date=models.DateTimeField(auto_now_add=True)
     location = models.ForeignKey(Location,on_delete=models.CASCADE)
     cartegory = models.ForeignKey(Cartegory,on_delete=models.CASCADE)
     
     def __str__(self):
         return self.image_name
     class Meta:
         ordering=['upload_date']
     @classmethod
     def search_by_image_category(cls,search_photo):
         photo=cls.objects.filter(category = search_photo)
         return photo  
 
     def search_by_location(cls,search_term):
        results = cls.objects.filter(location__icontains=search_term)  
        return results
