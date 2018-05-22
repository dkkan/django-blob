from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404

from myapp.models import Post


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('list.html')
    context = {'posts': posts}
    body = template.render({'posts': posts})
    return HttpResponse(body, content_type="text/html")

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)

