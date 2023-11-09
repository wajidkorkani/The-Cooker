from django.db import models

# Create your models here.
class CookingBlog(models.Model):
    image = models.ImageField(upload_to='media')
    recipe_name = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.recipe_name
