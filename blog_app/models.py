from django.db import models
from tinymce import models as tinymce_models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = tinymce_models.HTMLField()
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
