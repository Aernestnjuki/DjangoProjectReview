from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    # owner =
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # featured_image = models.ImageField()
    demo_link = models.CharField(max_length=255, null=True, blank=True)
    source_link = models.CharField(max_length=255, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_ration = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


# these model has a one_to_one relationship
class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down')
    )

    # owner
    project =models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=True, blank=True) # after deleting a project, delete associate reviews also
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name