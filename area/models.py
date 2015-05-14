from django.db import models

# Create your models here.
class description(models.Model):    
    description_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    submitter = models.CharField(max_length=300)


class area_map(models.Model):
    map_field = models.TextField()
    notes = models.TextField()


class quest(models.Model):
    description_text = models.TextField()
