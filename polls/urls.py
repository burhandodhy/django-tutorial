from django.urls import path
from . import views

# # Old code
# app_name = 'polls'
# urlpatterns = [

#   # /polls/
#   path('',views.index, name="index"),

#   #/polls/ID
#   path('<int:question_id>/', views.detail, name="detail"),

#   #polls/ID/result
#   path('<int:question_id>/results', views.results, name='results'),

#   #polls/ID/vote
#   path('<int:question_id>/vote', views.vote, name="vote")
# ]


# Generic Viewsapp_name = 'polls'
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]