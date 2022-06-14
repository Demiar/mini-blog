from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/bloggers/', AuthorListView.as_view(), name='author_list'),
    path('blog/bloggers/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    # path('login/', Login.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]