from django.db import models
from authentication.models import User


class Review(models.Model):
    rating = models.PositiveSmallIntegerField(null=True)
    description = models.CharField(max_length=200, null = True, blank =True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    reviewed_by = models.ForeignKey(User, related_name="review_likes", on_delete=models.CASCADE, null=True)
    postive_experience = models.ManyToManyField(User, related_name="positive_experiences", )
    negative_experience = models.ManyToManyField(User, related_name="negative_experiences", )


    def __str__(self):
        return str(self.created)

    def num_of_rewiews(self):
        return self.reviewed_by.all().count()

    def positive_likes(self):
        return self.postive_experience.all().count()

    def negative_likes(self):
        return self.negative_experience.all().count()

    class Meta:
        ordering = ['-created']