from django.db import models
from django.utils.timezone import now

# Create your models here.

class StatusInfo(models.Model):
      sno = models.AutoField(primary_key=True)
      name = models.TextField()
      Artist = models.TextField()
      cover_image = models.ImageField(default="2.jpg", null=True, blank=True, upload_to='cover_image')
      description = models.TextField(blank=True, null=True)
      link = models.TextField()
      timestamp = models.DateTimeField(default=now)

      def __str__(self):
          return self.name
      
