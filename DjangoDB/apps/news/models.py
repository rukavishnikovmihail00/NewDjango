from django.db import models

class Articles(models.Model): # создание модели автоматически вызывает создание таблицы в БД
    title = models.CharField(max_length=120) 
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):  # при обращении к title возвращает значение, а не объект
        return self.title

