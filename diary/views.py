import datetime
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect 

from django.utils import timezone

from .forms import BlogPostModelForm, CommentForm
from .models import BlogPost, Comment



def superuser_only(function):
   def _inner(request, *args, **kwargs):
       if not request.user.is_superuser:
           raise PermissionDenied           
       return function(request, *args, **kwargs)
   return _inner


def blog_post_list_view(request):
    qs = BlogPost.objects.all().published().order_by('-publish_date')
    current_time = timezone.now()
    start_time = current_time - datetime.timedelta(days=700)
    blog_post_filter = BlogPost.objects.filter(publish_date__gte=start_time).order_by('-publish_date')
    blog_post_filter_older = BlogPost.objects.filter(publish_date__lte=start_time).order_by('-publish_date')
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'diary/list.html'
    context = { 'object_list': qs, 'post_filter': blog_post_filter, 'old_filter': blog_post_filter_older}
    return render(request, template_name, context)


@superuser_only
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'diary/form.html'
    context = {'form': form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    user = request.user
    obj = get_object_or_404(BlogPost, slug=slug)
    comments = Comment.objects.filter(post=obj)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST or None)
        if comments:
            messages.warning(request, f"I'm afraid you cannot comment twice {user}")
            # raise PermissionDenied('you have already commented')
            return redirect(f"/diary/{slug}")
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post=obj
            )
            comment.save()
            messages.success(request, f"Thank you for your comment{user}")
        else:
            messages.warning(request, f"I'm afraid something went wrong{user}")
    else:
        form = CommentForm()

    context = {
        'object': obj,
        'comments': comments,
        'form': form 
        
        }
    template_name = 'diary/detail.html'
    
    return render(request, template_name, context)

@superuser_only
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/diary/')
    template_name = 'diary/form.html'
    context = { 'title': f"Update {obj.title}", "form":form}
    return render(request, template_name, context)


@superuser_only
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'diary/delete.html'
    if request.method == 'POST':
        obj.delete()
        return redirect('/diary')
    context = {
        'object': obj
    }
    return render(request, template_name, context)  