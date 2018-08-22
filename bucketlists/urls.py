from django.conf.urls import url
from django.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import BucketlistCreateView, BucketlistDetailsView

urlpatterns = {
    url(r'^create/$', BucketlistCreateView.as_view(), name="create"),
    url(r'^details/(?P<pk>[0-9]+)/$', BucketlistDetailsView.as_view(), name="details"),
    #url(r'^users/$', UserView.as_view(), name="users"),
    #url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
