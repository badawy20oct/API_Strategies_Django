from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, related_name = 'reviews', on_delete = models.CASCADE)
    reviewer = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer} - {self.book.title}"
