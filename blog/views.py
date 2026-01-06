from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView,  ListView, DetailView

# Create your views here.


def home(request):
    posts = Post.objects.all()
    
    context = {'posts': posts, 'title':'Blog Home'}
    return render(request, 'blog/home.html', content_type='text/html', context=context)


# CBV for listing posts class based View = cbv
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-published_date']

    paginate_by = 5

# CBV for listing posts of a particular user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-published_date']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-published_date')

    paginate_by = 5




class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', context={'title':'About Page'})


class createPost(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']

    # assign the logged in user as author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    


class deletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class updatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # assign the logged in user as author of the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    

    # prevent any unauthorized user from updating posts of other users
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False    

