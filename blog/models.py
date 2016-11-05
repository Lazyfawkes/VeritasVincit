from django.db import models
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, default='')

    def __str__(self):
        return self.name

    
class MyBlog(models.Model):
    author = models.ForeignKey('auth.User', default='Anonymous')
    title = models.CharField(max_length=255)
    text = models.TextField()    
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
# Create your models here.
