import uuid
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView, View, TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from App_Blog.models import Blog, Comment, Like

# Create your views here.



class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'App_Blog/blog_details.html', context={'blog':blog})
