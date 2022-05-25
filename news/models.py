from django.db import models
import datetime as dt


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()


class Tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_img = models.ImageField(null=True, blank=True, upload_to='articles/')

    def __str__(self):
        return self.title

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls, date):
        news = Article.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls, search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news
