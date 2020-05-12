from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('addproperty/',views.addproperty, name='addproperty'),
    path('addcomment/<int:id>',views.propertycomment, name='propertycomment'),
    path('addgaleri/<int:id>',views.addgaleri, name='addgaleri'),
    # ex: /home/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /home/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /home/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]