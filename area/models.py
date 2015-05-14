from django.db import models
    
# Create your models here.
class Description(models.Model):    
    description_text = models.TextField()
    pub_date = models.DateTimeField('date published')
    submitter = models.CharField(max_length=300)


class Area_map(models.Model):
    map_field = models.TextField()
    notes = models.TextField()


class Quest(models.Model):
    description_text = models.TextField()

class User(models.Model):
    name = models.CharField(max_length=250)
    character = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    passwd = models.CharField(max_length=250)

class Area(models.Model):
    area_map = models.ForeignKey(Area_map)
    description = models.ForeignKey(Description)
    quest = models.ForeignKey(Quest)
