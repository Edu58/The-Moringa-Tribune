from django.test import TestCase
from .models import Editor, Article, Tags
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):
    def setUp(self) -> None:
        self.john = Editor(first_name='john', last_name='doe', email='johndoe@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.john, Editor))

    def test_save_method(self):
        self.john.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ArticleTestClass(TestCase):
    def setUp(self) -> None:
        # create new editor
        self.john = Editor(first_name='john', last_name='doe', email='johndoe@gmail.com')
        self.john.save_editor()

        # create new tags
        self.new_tag = Tags(name='soccer')
        self.new_tag.save()

        # create new article
        self.new_article = Article(title='Aresenal killed in action',
                                   post='Arsenal was laid flat on the floor bleeding and crying in the 5th corner of the EPL street',
                                   editor=self.john)
        self.new_article.save()

        # Add tags to new_article
        self.new_article.tags.add(self.new_tag)

    # remove the changes after test
    def tearDown(self) -> None:
        Editor.objects.all().delete()
        Article.objects.all().delete()
        Tags.objects.all().delete()

    # Actual tests
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2022-01-12'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
