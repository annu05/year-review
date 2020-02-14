from django.db import models
from django.contrib.auth.models import User


class Anime(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    DATE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
    )
    MONTH = (
        (1, 'jan'),
        (2, 'feb'),
        (3, 'mar'),
        (4, 'apr'),
        (5, 'may'),
        (6, 'jun'),
        (7, 'jul'),
        (8, 'aug'),
        (9, 'sep'),
        (10, 'oct'),
        (11, 'nov'),
        (12, 'dec'),
    )
    YEAR = (
        (1, '2020'),
        (2, '2019'),
    )
    animeid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    image = models.URLField(default='')
    rating = models.IntegerField(choices=RATING_CHOICES,default=1)
    startdate = models.IntegerField(choices=DATE ,default=1)
    startmonth = models.IntegerField(choices=MONTH,default=1)
    startyear = models.CharField(max_length=10,default=1)
    enddate = models.IntegerField(choices=DATE, default=1)
    endmonth = models.IntegerField(choices=MONTH, default=1)
    endyear = models.IntegerField(choices=YEAR, default=1)
    episode = models.IntegerField(default=12)

    def __str__(self):
        return self.title

class Movie(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    DATE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
    )
    MONTH = (
        (1, 'jan'),
        (2, 'feb'),
        (3, 'mar'),
        (4, 'apr'),
        (5, 'may'),
        (6, 'jun'),
        (7, 'jul'),
        (8, 'aug'),
        (9, 'sep'),
        (10, 'oct'),
        (11, 'nov'),
        (12, 'dec'),
    )
    YEAR = (
        (1, '2020'),
        (2, '2021'),
    )
    movieid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    image = models.URLField(default='')
    rating = models.IntegerField(choices=RATING_CHOICES,default=1)
    date = models.IntegerField(choices=DATE ,default=1)
    month = models.IntegerField(choices=MONTH,default=1)
    year = models.CharField(max_length=10,default=2020)

    def __str__(self):
        return self.title



class Manga(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    MONTH = (
        (1, 'jan'),
        (2, 'feb'),
        (3, 'mar'),
        (4, 'apr'),
        (5, 'may'),
        (6, 'jun'),
        (7, 'jul'),
        (8, 'aug'),
        (9, 'sep'),
        (10, 'oct'),
        (11, 'nov'),
        (12, 'dec'),
    )
    YEAR = (
        (1, '2020'),
    )
    mangaid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    image = models.URLField(default='')
    rating = models.IntegerField(choices=RATING_CHOICES,default=1)
    month = models.IntegerField(choices=MONTH,default=1)
    year = models.IntegerField(choices=YEAR,default=1)

    def __str__(self):
        return self.title

class Book(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    MONTH = (
        (1, 'jan'),
        (2, 'feb'),
        (3, 'mar'),
        (4, 'apr'),
        (5, 'may'),
        (6, 'jun'),
        (7, 'jul'),
        (8, 'aug'),
        (9, 'sep'),
        (10, 'oct'),
        (11, 'nov'),
        (12, 'dec'),
    )
    YEAR = (
        (1, '2020'),
    )
    bookid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    image = models.URLField(default='')
    rating = models.IntegerField(choices=RATING_CHOICES,default=1)
    month = models.IntegerField(choices=MONTH,default=1)
    year = models.IntegerField(choices=YEAR,default=1)

    def __str__(self):
        return self.title


class Drawing(models.Model):
    DATE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
        (11, '11'),
        (12, '12'),
        (13, '13'),
        (14, '14'),
        (15, '15'),
        (16, '16'),
        (17, '17'),
        (18, '18'),
        (19, '19'),
        (20, '20'),
        (21, '21'),
        (22, '22'),
        (23, '23'),
        (24, '24'),
        (25, '25'),
        (26, '26'),
        (27, '27'),
        (28, '28'),
        (29, '29'),
        (30, '30'),
        (31, '31'),
    )

    MONTH = (
        (1, 'jan'),
        (2, 'feb'),
        (3, 'mar'),
        (4, 'apr'),
        (5, 'may'),
        (6, 'jun'),
        (7, 'jul'),
        (8, 'aug'),
        (9, 'sep'),
        (10, 'oct'),
        (11, 'nov'),
        (12, 'dec'),
    )
    YEAR = (
        (1, '2020'),
    )
    drawingid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique=True)
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    date = models.IntegerField(choices=DATE, default=1)
    month = models.IntegerField(choices=MONTH,default=1)
    year = models.IntegerField(choices=YEAR,default=1)

    def __str__(self):
        return self.title
