from django.urls import path
from .views import HomeView,NewPostView,PostDetailView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', HomeView.as_view() , name="home"),
    path('post/new/', NewPostView.as_view() , name="post_new"),
    path('post/<int:pk>', PostDetailView.as_view() , name="post_detail"),
    path('post/update/<int:pk>', PostUpdateView.as_view() , name="update"),
    path('post/delete/<int:pk>', PostDeleteView.as_view() , name="delete"),
]
