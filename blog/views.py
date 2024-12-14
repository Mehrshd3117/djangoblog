from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.all()
    paginate_by = 2


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(Post.objects.filter(publish_time__year=self.kwargs['year'],
                                                     publish_time__month=self.kwargs['month'],
                                                     publish_time__day=self.kwargs['day'],
                                                     slug=self.kwargs['slug']))

#
# get_object_or_404(
#             Post.objects.filter(publish_time__year=self.kwargs['year'],
#                                 publish_time__month=self.kwargs['month'], publish_time__day=self.kwargs['day'],
#                                 slug=self.kwargs['slug']))
