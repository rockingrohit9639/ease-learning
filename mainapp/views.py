from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def resources(request):
    cources = Courses.objects.all()
    semester = Semesters.objects.all()
    context = {
        "cources": cources,
        "semesters":semester,
    }
    return render(request, 'resources.html', context)


def get_resources(request, sem):
    all_res = Resources.objects.filter(sem=sem)
    context = {
        "resources":all_res,
    }
    return render(request, 'get_resource.html', context)


def add_requirements(request):
    name = request.GET['name']
    email = request.GET['email']
    req = request.GET['req']
    new_req = User_Requirements(name=name, email=email, resource=req)
    new_req.save()
    return redirect(request.path)


def about(request):

    return render(request, 'about.html')


def feedback(request):
    name = request.GET['name']
    email = request.GET['email']
    feedback = request.GET['feedback']
    new_feed = Feedbacks(name=name, email=email, feedback=feedback)
    new_feed.save()

    return redirect(request.path)


def hande_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['inputPassword']
        next = request.POST.get('next', '/')
        user = authenticate(request, username=username, password=passw)
        if user is not None:
            login(request, user)
            if next == "/search":
                return redirect('/')
            else:
                return redirect(next)
        else:
            return redirect(request.path)
    return redirect('/')


def handle_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        passw = request.POST['password']
        next = request.POST.get('next', '/')

        user = User.objects.create_user(username=uname, email=email, password=passw)
        user.first_name = fname
        user.last_name = lname
        user.save()

    return redirect(next)


def handle_logout(request):
    n = request.META.get('HTTP_REFERER')

    logout(request)
    if n == "http://127.0.0.1:8000/admin_panel":
        return redirect('/')
    else:
        return HttpResponseRedirect(n)


def search(request):
    query = request.GET['qry']
    res = Resources.objects.filter(name__icontains=query)

    context = {
        "resources":res,
    }
    return render(request, 'search.html', context)


def blog(request):
    all_posts = Blog.objects.all()
    context = {
        "posts":all_posts,
    }
    return render(request, 'blog.html', context)


def post(request, slug):
    post = Blog.objects.get(slug=slug)
    all_posts = Blog.objects.all()
    context = {
        "post":post,
        "allPosts":all_posts,
    }
    return render(request, 'blogpost.html', context)


def add_post(request):
    return render(request, 'new_post.html')

def add_new_post(request):
    title = request.GET['title']
    sub_title = request.GET['subutitle']
    desc = request.GET['desc']
    slug = request.GET['slug']
    user_name = request.GET['user']
    user = User.objects.get(username=user_name)

    new_post = Blog(title=title, subtitle=sub_title, description=desc, slug=slug, user=user)
    new_post.save()

    return redirect('/')

def admin_panel(request):
    user_name = request.user
    user = User.objects.get(username=user_name)
    posts = Blog.objects.filter(user=user)
    context = {
        "posts":posts,
    }
    return render(request, 'admin.html', context)


def edit_page(request, slug):
    post = Blog.objects.get(slug=slug)
    context = {
        "post":post,
    }
    return render(request, 'edit_page.html', context)


def edit_post(request):
    new_title = request.GET['title']
    new_sub_title = request.GET['subutitle']
    new_desc = request.GET['desc']
    new_slug = request.GET['slug']
    user_name = request.GET['user']
    id = request.GET['id']
    user = User.objects.get(username=user_name)
    post = Blog.objects.get(id=id)
    post.title = new_title
    post.subtitle = new_sub_title
    post.description = new_desc
    post.slug = new_slug
    post.user = user
    post.save()

    return redirect('/admin_panel')

def delete(request, slug):
    post = Blog.objects.get(slug=slug)
    post.delete()
    return redirect('/admin_panel')