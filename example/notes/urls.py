from django.urls import path
from notes import views

urlpatterns = [

    # regular Django views
    path('notes1/', views.notes_list1),
    path('notes1/<int:pk>/', views.notes_detail1),

    # @api_view
    path('notes2/', views.notes_list2),
    path('notes2/<int:pk>/', views.notes_detail2),

    # APIView
    #path('notes3/', views.notesList1.as_view()),
    #path('notes3/<int:pk>/', views.notes_detail1.as_view()),

    # GenericAPIView + Mixins
    #path('notes4/', views.notesList2.as_view()),
    #path('notes4/<int:pk>/', views.notes_detail2.as_view()),

    # Concrete view classes
    #path('notes5/', views.notesList3.as_view()),
    #path('notes5/<int:pk>/', views.notes_detail3.as_view()),

]