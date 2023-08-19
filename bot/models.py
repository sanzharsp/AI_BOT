from django.db import models
from ckeditor.fields import RichTextField



class SystemTextModal(models.Model):
    content = RichTextField(verbose_name="Задача для телеграм бота")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания")
    # Временная метка показывающая время последнего обновления объекта.
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Дата последнего изменения")
    def __str__(self):
        return "{}".format(self.id) 
    
    class Meta:
        ordering = ['id']
        verbose_name='роль для телеграм бота'
        verbose_name_plural='Задачи телеграм бота'



# Create your models here.
class UserId(models.Model):
    user_id = models.IntegerField(default= 0, verbose_name= "Уникальный идентификатор в телеграм", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания")
    # Временная метка показывающая время последнего обновления объекта.
    updated_at = models.DateTimeField(auto_now=True, verbose_name = "Дата последнего изменения")
    def __str__(self):
        return "{}".format(self.user_id)     

    class Meta:
        ordering = ['user_id']
        verbose_name='данные пользователя телеграм бота'
        verbose_name_plural='Данные пользователя телеграм бота'


class MessageText(models.Model):
    user_id = models.ForeignKey(UserId, related_name = 'user_id_text', verbose_name="Уникальный идентификатор", on_delete=models.CASCADE)
    userText = models.TextField(verbose_name="Текст пользователя телеграм бота",  max_length=1000000)
    assistantText = models.TextField(verbose_name="Текст асистента телеграм бота",  max_length=1000000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания")

    def __str__(self):
        return "{}".format(self.user_id)     

    class Meta:
        ordering = ['user_id']
        verbose_name='переписку'
        verbose_name_plural='Переписка'