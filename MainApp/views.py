from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment 
from .forms import PizzaForm, CommentForm 

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html') 

def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas} 

    return render(request, 'MainApp/pizzas.html', context) 

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('pizza_id') 
    picture = pizza.picture

    #comments= pizza.comment_set.all().order_by('-date_added')

    context = {'pizza':pizza, 'toppings':toppings, 'picture':picture, 'comments':comments} 

    return render(request, 'MainApp/pizza.html', context)

def new_comment(request, pizza_id):
  
    new_comment = Pizza.objects.get(id=pizza_id)
    

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False) 
            new_comment.comment = new_comment 
            new_comment.save() 
            return redirect('MainApp:pizza', pizza_id=pizza_id)  

    context = {'form':form, 'comment':new_comment}
    return render(request, 'MainApp/new_comment.html', context)


def comments(request, pizza_id):
    if request.method == 'POST' and request.POST.get('btn1'):
        comment = request.POST.get('comment') 
        Comment.objects.create(pizza_id=pizza_id,text=comment)


    comments = Comment.objects.filter(pizza_id=pizza_id)
    post = Pizza.objects.get(id=pizza_id)

    context = {'post':post, 'comments':comments} 
    
    return render(request, 'MainApp/comments.html',context)