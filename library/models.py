from django.db import models


# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=50, null=False, blank=False)
    birthday = models.DateTimeField(null=True, blank=True)
    death_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return f"{self.author}"


class Book(models.Model):
    book = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey(
        'library.Author',
        related_name='books',
        on_delete=models.CASCADE,
        verbose_name='Автор',
        default=1
    )
    genre = models.ManyToManyField(
        'library.Genre',
        related_name='genres',
        blank=False,
        default=1
    )

    published_at = models.DateTimeField(null=True, blank=False)


class Genre(models.Model):
    genre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return '{}. {}'.format(self.pk, self.genre)
