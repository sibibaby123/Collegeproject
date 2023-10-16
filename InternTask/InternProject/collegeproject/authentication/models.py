from django.db import models
from django.urls import reverse
# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='department',unique=True)
    email=models.EmailField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='departments'

    def __str__(self):
        return '{}'.format(self.name)

class Purpose(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    contact=models.TextField(blank=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='course',unique=True)
    email=models.EmailField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering=('name',)
        verbose_name='purpose'
        verbose_name_plural='purposes'

    def __str__(self):
        return '{}'.format(self.name)

