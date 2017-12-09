from django.conf.urls import url

from core.views import ChannelView, CategoryView

urlpatterns = [
    url(r'^$', ChannelView.as_view()),
    url(r'^(?P<slug>[\w-]+)/categories/$', CategoryView.as_view()),
]
