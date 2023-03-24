import enum
from uuid import uuid4

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='0000-10-01')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='genres')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='languages')

    def __str__(self):
        return self.title


class Genre(models.Model):
    GENRE_CHOICES = [
        ('DEVELOPER', 'DEV'),
        ('FINANCE', 'FIN'),
        ('ADVENTURE', 'ADV'),
        ('DRAMA', 'DRA'),
        ('FANTASY', 'FAN'),
        ('THRILLER', 'THR'),
        ('BIOGRAPHY', 'BIO'),
    ]
    name = models.CharField(max_length=30, choices=GENRE_CHOICES, default='DEV')

    def __str__(self):
        return self.name


class Language(models.Model):
    LANGUAGE_CHOICES = [
        ('ENGLISH', 'ENG'),
        ('FRENCH', 'FRE'),
        ('SPANISH', 'SPA'),
        ('YORUBA', 'YOR'),
        ('IGBO', 'IGB'),
        ('HAUSA', 'HAU')
    ]
    name = models.CharField(max_length=15, choices= LANGUAGE_CHOICES, default='EN')

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    # todo Drop down in django
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]
    # todo overiding django id
    unique_id = models.UUIDField(default=uuid4)
    due_back = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='books')
    imprint = models.CharField(max_length=55, blank=False, null=False)

    # borrower = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='borrower')

    def __str__(self):
        return self.imprint
