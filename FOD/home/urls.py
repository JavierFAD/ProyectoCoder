
from home import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='Home'),
    path("about/", views.about, name='About'),
    path("contact/", views.contact, name='Contact'),
    path("post/", views.post, name='Post'),
    path("post_2/", views.post2, name='Post-2'),  
]
