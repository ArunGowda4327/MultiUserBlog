from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')



class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post
    template_name = 'blog/create_post.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post
    template_name = 'blog/create_post.html'


class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = reverse_lazy('post_list')
    context_object_name = 'post'
    template_name = 'blog/post_remove.html'


class PostDraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft_list.html'


    model = Post
    context_object_name = 'draft_post'
    template_name = 'blog/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')





@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
##########################
#COMMENT SECTION
##########################
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/create_comment.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    saving = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=saving)
