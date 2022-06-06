from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    text = models.TextField(verbose_name='texts')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='pub_dates')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='authors'
    )
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL, related_name="group_posts",
        blank=True, null=True, verbose_name='groups'
    )

    class Meta:
        ordering = ['-pub_date']


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
