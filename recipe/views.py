from django.shortcuts import render, redirect
from django.views import View
from .models import Recipe, Ingredient,Contact, CommentRecipe
import requests
from django.urls  import reverse


class Home(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        two_recipes = Recipe.objects.all().order_by()[:2]
        context = {'recipes': recipes,'two_recipes': two_recipes}
        return render(request, 'index.html', context)

class About(View):
    def get(self, request):
        return render(request, 'about.html')

class BlogPost(View):
    def get(self, request):
        return render(request, 'blog-post.html')
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        self.send_telegram_message(name, email, subject, message) 
        return render(request, 'index.html', {'success': 'Your message has been sent'})


    def send_telegram_message(self, name, email, subject, message):
        bot_token = '7103821725:AAEeh30tBRyByHozOg0EdNBhUFDiSv4ngEw'
        chat_id = 1913322681
        telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        
        xabar = f'Yangi xabar keldi\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'

        payload = {
            'chat_id': chat_id,
            'text': xabar
        }
        response = requests.post(url=telegram_api_url, data=payload)
        if response.status_code != 200:
            print(f'Error sending message: {response.status_code}, Response: {response.text}')


class RecipeList(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        context = {'recipes': recipes}
        return render(request, 'recipe-list.html', context)
class Elements(View):
    def get(self, request):
        return render(request, 'elements.html')

class Recipe_Post(View):
    
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        return render(request, 'receipe-post.html', {'recipe': recipe})

    def post(self, request , id):
        recipe  = Recipe.objects.get('message')
        user  = request.user
        message = request.POST.get('message')
        CommentRecipe.objects.create(user=user, recipe=recipe, text=message)
        return redirect(reverse('recipe-post'),kwargs={'id': id})
    


class RecipeDetail(View):
    def get(self, request, id):
        recipe = Recipe.objects.get(id=id)
        comments = CommentRecipe.objects.filter(recipe=recipe)
        return render(request, 'receipe-post.html', {'recipe': recipe, 'comments': comments})
    
    def post(self, request, id):
        recipe = Recipe.objects.get(id=id)
        user = request.user
        message = request.POST.get('message')
        rating = request.POST.get('rating')
        CommentRecipe.objects.create(user=user, recipe=recipe, text=message, rating=rating)
        return redirect(reverse('recipe-detail', kwargs={'id': id}))
    
    
    
    
    