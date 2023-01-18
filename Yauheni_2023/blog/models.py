from django.db import models

# Create your models here.
#  класс категории для связки категорий
class Category(models.Model):
    name = models.CharField(max_length=30)

# модель поста
class Post(models.Model):
    title = models.CharField(max_length=250)# название статьи
    body = models.TextField() #тело нашего поста, то что будет написано в основной части статьи
    created_on = models.DateTimeField(auto_now_add=True) # дата создания экземпляра класса
    last_modified = models.DateTimeField(auto_now=True) # время изменения нашего поста
    categories = models.ManyToManyField('Category', related_name='posts')# отношение многие к многим

# модель комментариев
class Comment(models.Model):
    author = models.CharField(max_length=30) # имя автора
    body = models.TextField() #тело комментария, основной текст
    created_on = models.DateTimeField(auto_now_add=True) # назначает текущую дату и время этому полю всякий раз, когда создается экземпляр этого класса
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

# после создания моделей,создаем файл миграции python manage.py makemigrations blog
# сохраняю python manage.py migrate
