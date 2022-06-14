from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField('Биография')

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return self.user.last_name + ' ' + self.user.first_name
        return self.user.username

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.pk)])

class Blog(models.Model):
    title = models.CharField('Название', max_length=250)
    post_date = models.DateTimeField('Дата публикации', auto_now=True)
    content = models.TextField('Контент')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-post_date']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.pk)])

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField('Текст сообщения')
    post_date = models.DateTimeField('Дата публикации', auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'