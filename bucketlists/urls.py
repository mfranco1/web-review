from django.conf.urls import url
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistCreateView

urlpatterns = {
    url(r'^create/$', BucketlistCreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
