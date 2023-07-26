from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView

from .forms import CommentForm
from .models import Post, Comment


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

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        context['comments'] = Comment.objects.filter(post=self.get_object(), approved=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, year, month, day, slug):
        post = self.get_object()
        comment_data = CommentForm(request.POST)
        if comment_data.is_valid():
            comment = Comment(post=post,
                              name=comment_data.cleaned_data['name'],
                              email=comment_data.cleaned_data['email'],
                              body=comment_data.cleaned_data['body']
                              )
            comment.save()
            self.object = self.get_object()
            return self.render_to_response(context=self.get_context_data())
        else:
            self.object = self.get_object()
            context = self.get_context_data()
            context['comment_form'] = comment_data
            return self.render_to_response(context=context)
