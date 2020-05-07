from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name="user_update"),
    path('password/', views.change_password, name="change_password"),
    path('properties/', views.properties, name="properties"),
    path('propertydetail/<int:id>', views.propertydetail, name="propertydetail"),
    path('comments/', views.comments, name="comments"),
    path('deletecomment/<int:id>', views.deletecomment, name="deletecomment"),

    # ex: /home/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /home/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /home/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]