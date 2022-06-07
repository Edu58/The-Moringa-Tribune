from urllib import response
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, JsonResponse
import datetime as dt
from .models import Article, NewsletterRecipients
from .forms import NewletterForm, NewArticleForm
from .email import send_welcome_email


# Create your views here.
def all_news(request):
    news = Article.objects.all()
    return render(request, 'news/all-news.html', {'news': news})


@login_required(login_url='/accounts/login/')
def article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'news/article.html', {'article': article})


def news_of_the_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    if request.method == 'POST':
        form = NewletterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            recipient = NewsletterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            HttpResponseRedirect('today')
    else:
        form = NewletterForm()
    return render(request, 'news/today-news.html', {"date": date, 'news': news, 'form': form})


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


@login_required(login_url='/accounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('today')

    else:
        form = NewArticleForm()
    return render(request, 'news/new_article.html', {"form": form})


def newletter(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    
    recipient = NewsletterRecipients(name=name, email=email)
    recipient.save()
    # send_welcome_email(email, email)
    data = {'success': 'You have been successfully added to our newletter list'}
    return JsonResponse(data)