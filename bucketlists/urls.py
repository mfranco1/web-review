from django.conf.urls import url
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistCreateView, BucketlistDetailsView

urlpatterns = {
    url(r'^create/$', BucketlistCreateView.as_view(), name="create"),
    url(r'^details/(?P<pk>[0-9]+)/$', BucketlistDetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
