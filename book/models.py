from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    create_time = models.DateTimeField(auto_created=True)
    update_time = models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name = "图书"
        verbose_name_plural = "图书"

    def __str__(self):
        return self.title


