from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth import get_user_model
from .utils import get_filename_ext,upload_image_path
User = get_user_model()

class Tweets(models.Model):
    # user
    tweet = models.TextField()
    # photo = models.ImageField(upload_to = '')

