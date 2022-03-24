from django.shortcuts import render
from blog.models import Post
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
 

# Function based views
def home(request):

    ''' Send data to the templates '''
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }

    return render(request, 'blog/home.html', context)

# Class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # set the form author
    # if we not set the get_absolute_url int the model
    # then it will shows 'No URL to redirect to.  Either provide a 
    # url or define a get_absolute_url method on the Model.' this error
    # so we need to set reverse method in the Model for getting 
    # the full URL

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {
        'title': 'About',
    }

    return render(request, 'blog/about.html', context)