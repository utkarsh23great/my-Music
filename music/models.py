from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Album(models.Model):
    title=models.CharField(max_length=100,null=False,help_text='album title')
    artist=models.CharField(max_length=100,help_text='album artist')
    genre=models.CharField(max_length=50,help_text='album genre')
    year=models.DateField(help_text='album year')
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png'])],default='')


    def __str__(self):
        return self.title

class Song(models.Model):
    al_id=models.ForeignKey(Album,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,help_text='song tilte')
    artist=models.CharField(max_length=100,help_text='song artist')
    genre=models.CharField(max_length=20,help_text='song genre')
    sfile=models.FileField(validators=[FileExtensionValidator(['mp3','aac'])])
    image=models.FileField(validators=[FileExtensionValidator(['jpg','png'])])
    def __str__(self):
        return self.title