from django.db import models


class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')


class User(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


class Blog(models.Model):
    Title = models.CharField(max_length=300)
    metaTitle = models.CharField(max_length=50)
    createdAt = models.CharField(max_length=50)
    updatedAt = models.CharField(max_length=50)
    content = models.CharField(max_length=2000)


class Comment(models.Model):
    postID = models.CharField(max_length=50)
    parentCommentID = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    createdAt = models.CharField(max_length=50)
    updatedAt = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
