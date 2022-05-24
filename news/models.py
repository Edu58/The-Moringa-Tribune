from django.db import models


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

    def __str__(self):
        return self.title