from django.db import models




class Books(models.Model):
    GENRE_CHOICE = (
        ('Детектив', 'Детектив'),
        ('Роман', 'Роман'),
        ('Детские', 'Детские')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите картинку',null=True)
    title = models.CharField(max_length=100, verbose_name='Напишите название книги')
    description = models.TextField(verbose_name='Напишите описание книги', default='Lorem Ipsum')
    price = models.FloatField(verbose_name='Укажите цену книги')
    date_published = models.DateField(verbose_name='Укажите дату публикации книги')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Детектив',verbose_name='Укажите жанр книги',null=True)
    pages = models.CharField(max_length=50, verbose_name='Укажите количество страниц в книге')
    author = models.CharField(max_length=30, verbose_name='Укажите автора книги')
    audio_book = models.URLField(verbose_name='Укажите ссылку на аудио-книгу')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
            return f'{self.title}-{self.price}$'

