from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, FormMixin
from django.contrib.auth import authenticate, login

from .models import Blog, Author
from .forms import *


class BlogListView(ListView):
    model = Blog
    paginate_by = 5


class BlogDetailView(FormMixin, DetailView):
    model = Blog
    form_class = CommentForm
    success_url = '/'

    def get_success_url(self):
        return '/'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = Comment(
                author=request.user,
                blog=self.object,
                text=form.cleaned_data['text']
            )
            comment.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(blog=self.object.pk).order_by('-post_date')
        context['form'] = self.get_form()
        return context


class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorDetailView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.filter(author=self.object.pk).order_by('-post_date')
        return context

class Login(FormView):
    form_class = LoginForm
    template_name = 'blog/login.html'
    success_url = '/'


    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)


class Register(LoginForm):
    template_name = 'blog/login.html'
    form_class = LoginForm