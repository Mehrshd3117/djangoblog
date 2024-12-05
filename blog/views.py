from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from models import Post


class BlogListView(ListView):
    context_object_name = 'post'
    queryset = Post.objects.filter(status=Post.StatusChoices.PUBLISHED, publish_time__lte=timezone.now())


class BlogDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(
            Post.objects.filter(status=Post.StatusChoices.PUBLISHED, publih_time__year=kwargs.get('year'),
                                publish_time__month=kwargs.get('month'), publish_time__day=kwargs.get('day'),
                                slug=self.object.slug))
