from django.conf.urls import url

from core.views import ChannelView, CategoryView, CategoryDetailView

urlpatterns = [
    url(r'^channels/$', ChannelView.as_view()),
    url(r'^channels/(?P<slug>[\w-]+)/categories/$', CategoryView.as_view()),

    url(r'^categories/(?P<uid>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$',
    CategoryDetailView.as_view()),
]
