from django.urls import path
from .import views
from .views import Recipe_Post



app_name = 'recipe' 
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog_post/', views.BlogPost.as_view(), name='blog_post'),
    path('elements/', views.Elements.as_view(), name='elements'),
    path('post/', Recipe_Post.as_view(), name='recipe_post'),
    path('recipe-detail/<int:id>/', views.RecipeDetail.as_view(), name='recipe-detail'),
]