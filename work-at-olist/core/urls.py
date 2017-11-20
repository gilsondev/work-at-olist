from django.conf.urls import url

from core.views import ChannelView

urlpatterns = [
    url(r'^$', ChannelView.as_view()),
]
