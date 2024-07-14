from django.db import models
# from django.contrib.auth.models import User
from django.db.models import F


class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=100)
    born_location = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    # popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    # def increase_popularity(self):
    #     Tag.objects.filter(id=self.id).update(popularity=F("popularity") + 1)


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    created_id = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote

    def all_tags(self):
        return Quote.objects.get(quote=self.quote).tags.all()

# Create your models here.
