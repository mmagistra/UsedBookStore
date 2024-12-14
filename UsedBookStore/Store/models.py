from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


"""
Models:
    User
        - user
    Book
        - title
        - description
        - cover
        - publisher
        - published_year
        - genres
        - authors
    BookInstance
        - book
        - condition
        - storage_cell
        - purchase_price
        - sale_price
    Condition
        - degree_of_wear
        - description
    Genre
        - name
    Author
        - name
"""


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/')
    publisher = models.CharField(max_length=255)
    published_year = models.IntegerField()

    genres = models.ManyToManyField(
        to=Genre,
        related_name='books',
    )
    authors = models.ManyToManyField(
        to=Author,
        related_name='books',
    )

    # instances - field for access to all the instances of the book

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='instances',
    )
    condition = models.ForeignKey(
        to='Condition',
        on_delete=models.PROTECT,
        related_name='book_instances',
    )
    storage_cell = models.CharField(max_length=50, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.book.title} - {self.storage_cell}"


class Condition(models.Model):
    degree_of_wear = models.IntegerField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.degree_of_wear

