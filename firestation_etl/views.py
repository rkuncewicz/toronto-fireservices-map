from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import twitter


def index(request):
    api = twitter.Api(
        consumer_key='',
        consumer_secret='',
        access_token_key='',
        access_token_secret=''
    )
    statuses = api.GetUserTimeline(
        screen_name='tofire',
        include_rts=False,
        exclude_replies=True,
        max_id='1065057734347948032'
    )
    print('1--------', statuses)
    return HttpResponse(" ".join(str(s.id) for s in statuses))
