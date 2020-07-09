from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """  """
    STATUC_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250) # строка длиной максимум 20 символов
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()


# Create your models here.
