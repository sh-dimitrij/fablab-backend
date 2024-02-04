from django.db import models
from django.contrib.auth.models import User # Для связи с таблицей User(создается автоматически в Django для авторизации)

# Create your models here.

class Participants(models.Model): # Модель(Таблица) Participants
    role = models.TextField(max_length=50) # Роль пользователя
    surname = models.TextField(max_length=50) # Фамилия пользователя
    name = models.TextField(max_length=50) # Имя пользователя
    patronymic = models.TextField(max_length=50) # Отчество пользователя
    age = models.IntegerField() # Возраст пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE) # user_id вторичный ключ для связи с таблицей с пользователями
    #(в БД она называется auth_user)
    class Meta:
        db_table = "participants"

class WorkTypes(models.Model): # Модель(Таблица) WorkTypes
    title = models.TextField() # Название услуги
    description = models.TextField() # Описание услуги
    price = models.IntegerField() # Цена услуги
    imageSource = models.TextField() # Путь к картинке на сервере, чтобы по нему выводить ее на сайте(в БД файлы как правило не хранятся)
    is_deleted = models.BooleanField(default=False) # Услуга удалена или нет
    class Meta:
        db_table = "worktypes"
    
class PrintOrders(models.Model): # Модель(Таблица) PrintOrders
    status = models.TextField(max_length=50) # Статус заявки
    dateCreate = models.DateTimeField() # Дата создания заявки, тип Date
    dateForm = models.DateTimeField() # Дата формирования заявки, тип Date
    dateEnd = models.DateTimeField() # Дата закрытия заявки, тип Date
    userData = models.ForeignKey(Participants, on_delete=models.CASCADE) # Связь с таблицей UserData (1:M), тип BigInt
    service = models.ManyToManyField(WorkTypes) # Здесь находится связь с таблицей Services (M:M), Django
    #по-умолчанию создает сводную таблицу при объявлении связи Многие ко многим, поэтому вручную ее создавать не надо
    #Также в Services нет такого поля, ибо Django создаст тогда 2 сводные таблицы, а смысл?) Нужна только одна!
    class Meta:
        db_table = "printorders"
    
    

    
