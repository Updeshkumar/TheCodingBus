from django.db import models
from django.urls import reverse


# Create your models here.
class blog(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    Conclusion = models.TextField()
    image = models.ImageField(upload_to ="media/images", blank=True)
    blog_vedio = models.FileField(upload_to ="media/vedio", blank=True)
    
    class Meta:
        verbose_name_plural = 'blogs'
        
    def get_absolute_url(self):
        return reverse('blogs:blog_detail', args=[self.slug])
        
    def __str__(self):
        return self.title
