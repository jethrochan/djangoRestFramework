from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from vessels import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^vessels/$', views.VesselList.as_view(), name='vessel-list'),
    url(r'^vesseldetail/(?P<pk>[0-9]+)/$', views.VesselDetail.as_view(), name='vessel-detail'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
