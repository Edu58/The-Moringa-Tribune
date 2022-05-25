from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_news, name='all_news'),
    path('article/<int:article_id>', views.article, name='article'),
    path('today/', views.news_of_the_day, name='today'),
    path('archives/<past_date>', views.past_days_news, name='pastNews'),
    path('search/', views.search, name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
