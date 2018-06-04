from django.conf.urls import url, include
from rest_framework import routers

from django.conf.urls import url
from myapp.views import list_view, detail_view, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


