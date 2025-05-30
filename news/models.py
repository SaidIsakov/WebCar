from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, unique=True)
    about_what = models.CharField(max_length=150, unique=True)
    text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'newses'