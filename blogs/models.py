from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=50)
    description = HTMLField()
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=255)
    Conclusion = models.TextField()
    meta_titile = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=200)
    focus_keyword = models.CharField(max_length=200)
    image = models.ImageField(upload_to ="media/images", blank=True)
    
    class Meta:
        verbose_name_plural = 'blogs'
        
    def get_absolute_url(self):
        return reverse('blogs:blog_detail', args=[self.slug])
        
    def __str__(self):
        return self.title
