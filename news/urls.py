from django.urls import path

from .views import news, news_tag_list, news_tag_details, news_item_details

app_name = 'news'

urlpatterns = [
    path('', news, name='news'),
    path('news/categories/', news_tag_list, name='news_tag_list'),
    path('news/category-details/<slug:slug>/', news_tag_details, name='news_tag_details'),
    path('news/<slug:item_slug>/', news_item_details, name='news_item_details'),
]
