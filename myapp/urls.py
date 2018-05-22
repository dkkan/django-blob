from django.conf.urls import url
from myapp.views import list_view, detail_view

urlpatterns = [
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
]

