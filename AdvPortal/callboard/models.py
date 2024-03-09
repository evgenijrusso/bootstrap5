from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
#from .utilites import get_timestamp_path


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True,
                                        verbose_name='Слать оповещения о новых комментариях?')

    # def delete(self, *args, **kwargs):
    #     for ad in self.advert_set.all():    # or adverts
    #         ad.delete()
    #     super().delete(*args, **kwargs)
    #
    # class Meta(AbstractUser.Meta):
    #     pass


class Advert(models.Model):  # Объявление
    author = models.ForeignKey(AdvUser, default='', on_delete=models.CASCADE,
                               verbose_name='Автор объявления', related_name='adverts')
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.PROTECT,
                                 verbose_name='Category')  # Категория
    title = models.CharField(max_length=100, verbose_name='Title')  # Заголовок
    content = models.TextField(verbose_name='Description')  # Описание
    price = models.FloatField(default=0, verbose_name='Price')  # Цена
    contacts = models.TextField(verbose_name='Contacts')  # Контакты
    # image = models.ImageField(blank=True, upload_to=get_timestamp_path,
    #                           verbose_name='Изображение')
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Show in list')  #Выводить в списке& ?
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Published')  # Опубликовано

    # def delete(self, *args, **kwargs):
    #     for ai in self.additionalimage_set.all():
    #         ai.delete()
    #     super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-created_at']


class AdditionalImage(models.Model):
    add_image = models.ForeignKey(Advert, on_delete=models.CASCADE,
                           verbose_name='Объявление')
    # image = models.ImageField(upload_to=get_timestamp_path,
    #                           verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Дополнительные иллюстрации'
        verbose_name = 'Дополнительная иллюстрация'


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True,
                            db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Comment(models.Model):
    ad = models.ForeignKey(Advert, on_delete=models.CASCADE,
                           verbose_name='Объявление')
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, db_index=True,
                                    verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['created_at']
