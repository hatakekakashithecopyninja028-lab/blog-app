from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Post, Category, Tag, Comment


def post_list(request):
    posts = Post.objects.filter(status='published').select_related('author', 'category')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    post.views += 1
    post.save(update_fields=['views'])
    
    comments = post.comments.filter(active=True)
    related_posts = Post.objects.filter(
        status='published', category=post.category
    ).exclude(id=post.id)[:3]
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        body = request.POST.get('body', '').strip()
        if name and email and body:
            Comment.objects.create(post=post, name=name, email=email, body=body)
            messages.success(request, 'Your comment has been posted!')
            return redirect(post.get_absolute_url())
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'related_posts': related_posts,
    })


def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(status='published', category=category)
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


def tag_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(status='published', tags=tag)
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/tag.html', {'tag': tag, 'posts': posts})


def search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(status='published')
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query) | Q(excerpt__icontains=query))
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/search.html', {'posts': posts, 'query': query})
