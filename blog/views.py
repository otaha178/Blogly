from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class BlogListView(View):
    template_name = 'home.html'
    paginate_by = 15

    def get(self, request, *args, **kwargs):
        blog_list = Post.objects.all()
        context = {'blog_list': blog_list}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class BlogDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


# Difference between put and patch? why does django use POST when updating?
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
