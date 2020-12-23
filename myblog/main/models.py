# Third-party imports
from precise_bbcode.fields import BBCodeTextField

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser


# Models
class AdvancedUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активация пройдена?')
    send_messages = models.BooleanField(default=True, verbose_name='Отправлять оповещения на почту?')

    class Meta(AbstractUser.Meta):
        pass


class PostCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(PostCategory, on_delete=models.PROTECT)
    author = models.ForeignKey(AdvancedUser, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    content = BBCodeTextField(null=True, blank=True, verbose_name='Текст поста')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_active = models.BooleanField(default=True, verbose_name='Выводить на сайте?')

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-created_at']