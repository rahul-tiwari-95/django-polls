from django.urls import path

from . import views

urlpatterns = [ 

    #home page OR polls/
    path('', views.index, name='index'),

    #polls/34/ --> Show question text with ID 34
    path('<int:question_id>', views.detail, name = 'detail'),

    #polls/34/results --> Show results of question_id 34
    path('<int:question_id>/results/', views.results, name= "results"),

    #polls/34/vote --> Allows us to vote on a particular question
    path('<int:question_id>/vote/', views.vote, name="vote")

]





#urlpatterns take 4 arguments'
#route + view + kwargs(optional) + name