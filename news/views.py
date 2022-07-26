from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import EditForm, CommentForm

# Create your views here.


class NewsView(ListView):
    """
        Displays news stories in a list
    """
    model = Post
    template_name = 'news-list.html'
    ordering = ['post_date']
    paginate_by = 6


class PostDetailView(DetailView):
    """
        Creates the views for the blog posts
    """
    model = Post
    template_name = 'post-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()

        return context


@login_required
class UpdatePostView(UpdateView):
    """
        Edit post view for editing/updating the blog
    """
    model = Post
    form_class = EditForm
    template_name = 'update-post.html'
    success_message = "{% name %} Your post has been successfully UPDATED"


@login_required
class DeletePostView(DeleteView):
    """
        Delete Posts from site
    """
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')


@login_required
class AddCommentView(SuccessMessageMixin, CreateView):
    """
        Create Add post view for creating blog posts on the site
    """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('base.html')
    success_message = "%{name} Your comment was Created Successfully"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
        success_message = "Your comment has been posted"
