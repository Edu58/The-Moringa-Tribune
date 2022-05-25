from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import Http404
import datetime as dt
from .models import Article


# Create your views here.
def all_news(request):
    news = Article.objects.all()
    return render(request, 'news/all-news.html', {'news': news})


def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'news/article.html', {'article': article})


def news_of_the_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'news/today-news.html', {"date": date, 'news': news})


def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', "Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    if date == dt.date.today():
        return redirect(news_of_the_day)

    news = Article.days_news(date)
    return render(request, 'news/past-news.html', {"date": date, 'news': news})


def search(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET['article']
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'
        return render(request, 'news/search.html', {'message': message, 'articles': searched_articles})
    else:
        message = "You haven't search for anything"
        return render(request, 'news/search.html', {'message': message})
