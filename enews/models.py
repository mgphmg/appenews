from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# ---------------------------
# Custom User Model
# ---------------------------
class User(AbstractUser):

    ROLE_CHOICES = (
        ('reader', 'Reader'),
        ('reporter', 'Reporter'),
        ('editor', 'Editor'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='reader')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    bio = models.TextField(blank=True)


# ---------------------------
# Category Model
# ---------------------------
class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ---------------------------
# Tags Model
# ---------------------------
class Tag(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# ---------------------------
# Article Model
# ---------------------------
class Article(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ---------------------------
# Article Media (Images/Videos)
# ---------------------------
class ArticleMedia(models.Model):

    MEDIA_TYPE = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='media'
    )

    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE)

    file = models.FileField(upload_to='article_media/')

    uploaded_at = models.DateTimeField(auto_now_add=True)


# ---------------------------
# Comments Model
# ---------------------------
class Comment(models.Model):

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    comment_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"


# ---------------------------
# Likes / Dislikes
# ---------------------------
class Reaction(models.Model):

    REACTION_CHOICES = (
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='reactions'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    reaction = models.CharField(max_length=10, choices=REACTION_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)


# ---------------------------
# Bookmark Model
# ---------------------------
class Bookmark(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookmarks'
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)


# ---------------------------
# Article Approval Workflow
# ---------------------------
class ArticleReview(models.Model):

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )

    editor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    remarks = models.TextField(blank=True)

    approved = models.BooleanField(default=False)

    reviewed_at = models.DateTimeField(auto_now_add=True)