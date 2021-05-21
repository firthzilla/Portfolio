from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import BlogPost


# Create your views here.

def home(request):
    blogPosts = BlogPost.objects.all()
    blogPost_list = []
    for blog in blogPosts:
      title = blog.title
      description = blog.description
      cover_image = blog.coverImage
      pub_date = blog.pub_date
      blogPost_list.append({
        'title': title,
        'description': description,
        'cover_image': cover_image,
        'pub_date': pub_date,
      })
    context = {
      'blogPost_list': blogPost_list
    }
    return render(request, 'home.html', context)


def contact(request):
    return render(request, 'contact.html')


def portfolio_list(request):
    blogPosts = BlogPost.objects.all()
    blogPost_list = []
    for blog in blogPosts:
      title = blog.title
      description = blog.description
      cover_image = blog.coverImage
      pub_date = blog.pub_date
      blogPost_list.append({
        'blog': blog,
        'title': title,
        'description': description,
        'cover_image': cover_image,
        'pub_date': pub_date,
      })
    context = {
      'blogPost_list': blogPost_list
    }
    return render(request, 'post_list.html', context)



def get_post(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if blog_post:
        context = {
            'blog': blog_post
        }
    return render(request, 'post_full.html', context)


