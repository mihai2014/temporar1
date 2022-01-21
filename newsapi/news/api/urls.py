from django.urls import path
from news.api.views import (article_list_create_api_view, 
                           article_detail_api_view)
from news.api.views import (ArticleListCreateAPIView,
                            ArticleDetailAPIView)


urlpatterns = [
    path('articles2/', 
         ArticleListCreateAPIView.as_view(), 
         name="article-list2"),
    path('articles2/<int:pk>/', 
         ArticleDetailAPIView.as_view(), 
         name="article-detail2"),

    path('articles1/', article_list_create_api_view, name="article-list1"),
    path('articles1/<int:pk>/', article_detail_api_view, name="article-detail1")
]    
