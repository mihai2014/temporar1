from django.urls import path
from snippets import views

urlpatterns = [
    # regular Django views
    path('snippets1/', views.snippet_list1),
    path('snippets1/<int:pk>/', views.snippet_detail1),

    # @api_view
    path('snippets2/', views.snippet_list2),
    path('snippets2/<int:pk>/', views.snippet_detail2),  

    # APIView
    path('snippets3/', views.SnippetList1.as_view()),
    path('snippets3/<int:pk>/', views.SnippetDetail1.as_view()),    

    # GenericAPIView + Mixins
    path('snippets4/', views.SnippetList2.as_view()),
    path('snippets4/<int:pk>/', views.SnippetDetail2.as_view()),

    # Concrete view classes
    path('snippets5/', views.SnippetList3.as_view()),
    path('snippets5/<int:pk>/', views.SnippetDetail3.as_view()),              
]

