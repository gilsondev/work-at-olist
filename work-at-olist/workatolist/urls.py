from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', include('rest_framework_docs.urls')),
    url(r'^api/channels/', include('core.urls')),
]
