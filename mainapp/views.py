from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify


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


def get_resources(request, sub):
    all_res = Resources.objects.filter(sub=sub)
    context = {
        "resources":all_res,
    }
    return render(request, 'get_resource.html', context)


def add_requirements(request):
    n = request.META.get('HTTP_REFERER')
    name = request.GET.get('name')
    email = request.GET.get('email')
    req = request.GET.get('req')
    try:
        new_req = User_Requirements(name=name, email=email, resource=req)
        new_req.save()
        messages.success(request, 'Your requirements has been sent to us successfully!')
        return HttpResponseRedirect(n)
    except Exception as e:
        messages.info(request, e)
        return HttpResponseRedirect(n)


def about(request):

    return render(request, 'about.html')


def feedback(request):
    n = request.META.get('HTTP_REFERER')
    name = request.GET.get('name')
    email = request.GET.get('email')
    feedback = request.GET.get('feedback')
    new_feed = Feedbacks(name=name, email=email, feedback=feedback)
    new_feed.save()
    messages.success(request, "Thanks for giving your feedback.")
    return HttpResponseRedirect(n)


def hande_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['inputPassword']
        next = request.POST.get('next', '/')
        user = authenticate(request, username=username, password=passw)
        if user is not None:
            messages.success(request, "Login Successfully!!")
            login(request, user)
            if next == "/search":
                return redirect('/')
            else:
                return redirect(next)
        else:
            messages.error(request, "Sorry!! Username or password does not match.")
            if next == "/search":
                return redirect('/')
            else:
                return redirect(next)
    return redirect('/')


def handle_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        passw = request.POST['password']
        next = request.POST.get('next', '/')

        try:
            user = User.objects.create_user(username=uname, email=email, password=passw)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request, "You have been signed up successfully. You can login now.")
            return redirect(next)
        except Exception as e:
            print(e)
            return redirect(next)


def handle_logout(request):
    n = request.META.get('HTTP_REFERER')

    logout(request)
    if n == "http://127.0.0.1:8000/admin_panel":
        messages.success(request, "Successfully Logged out.")
        return redirect('/')
    else:
        messages.success(request, "Successfully Logged out.")
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
    title = request.GET.get('title')
    sub_title = request.GET.get('subtitle')
    desc = request.GET.get('desc')
    slug = slugify(title)
    user_name = request.user
    user = User.objects.get(username=user_name)
    n = request.META.get('HTTP_REFERER')

    try:
        new_post = Blog(title=title, subtitle=sub_title, description=desc, slug=slug, user=user)
        new_post.save()
        messages.success(request, "Post Has been added successfully!!")
        return HttpResponseRedirect(n)

    except Exception as e:
        messages.error(request, e)
        return HttpResponseRedirect(n)


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

    messages.success(request, "Post has been edited successfully.")
    return redirect('/admin_panel')


def delete(request, slug):
    post = Blog.objects.get(slug=slug)
    post.delete()
    messages.info(request, "Post deleted successfully.")
    return redirect('/admin_panel')


def subjects(request, sem):
    all_subs = Subject.objects.filter(semester=sem)
    context = {
        "subjects":all_subs,
    }

    return render(request, 'subjects.html', context)