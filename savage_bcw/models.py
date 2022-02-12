from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    describe = models.TextField()
    composition = models.CharField(max_length=300)
    price = models.FloatField()

    def __str__(self):
        return f'{self.name}'


class Member(models.Model):
    nick_name = models.CharField(max_length=130)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    games = models.ManyToManyField('Game', related_name='member')

    def __str__(self):
        return f'{self.nick_name}'


class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Partner(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'