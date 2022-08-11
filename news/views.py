from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from .forms import EditForm

# Create your views here.


# recipe list view


class NewsView(ListView):
    """
        Displays news stories in a list
    """
    model = Post
    template_name = 'news-list.html'
    ordering = ['post_date']
    paginate_by = 6


# post detail view for recipes


class PostDetailView(DetailView):
    """
        Creates the views for the blog posts
    """
    model = Post
    template_name = 'post-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()

        return context


# update post view


class UpdatePostView(UpdateView):
    """
        Edit post view for editing/updating the blog
    """
    model = Post
    form_class = EditForm
    template_name = 'update-post.html'
    success_message = "{% name %} Your post has been successfully UPDATED"


# delete post view


class DeletePostView(DeleteView):
    """
        Delete Posts from site
    """
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
