from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.
# def list_view(request):
#     posts = Post.objects.filter(status='published', publish_time__lte=timezone.now())
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/list.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'


# def detail_view(request, year, month, day, slug):
#     post = get_object_or_404(Post, status='published', publish_time__year=year, publish_time__month=month,
#                              publish_time__day=day, slug=slug)
#     context = {
#         'post': post
#     }
#     return render(request, 'blog/detail.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return Post.objects.get(status='published', publish_time__year=self.kwargs['year'],
                                publish_time__month=self.kwargs['month'], publish_time__day=self.kwargs['day'],
                                slug=self.kwargs['slug'])
