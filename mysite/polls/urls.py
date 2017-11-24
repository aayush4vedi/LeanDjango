from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name="index"),
    # ex: /polls/
    url(r'^(?P<question_id>[0-9]+)/$',views.detail, name ="details"),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/results$',views.results, name ="results"),
     # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/votes$',views.votes, name ="votes"),
    # ex: /polls/5/vote/
]
