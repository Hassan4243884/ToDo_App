from django.db import models
from django.urls import reverse
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=31,unique=True)
    logo = models.TextField("logo")
    slug = models.SlugField()

    def __str__(self):
        return self.name



class Task(models.Model):
    title = models.CharField("title",max_length=99)
    details = models.TextField("details")
    tag = models.ForeignKey(Tag,related_name="tasks",on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-date_added",]
    
    def get_delete_url(self):
        return reverse("delete",kwargs={"pk":self.id})

    def get_update_url(self):
        return reverse("update",kwargs={"pk":self.id})
    
