from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User  # Import the User model
from django.contrib import messages
from .models import Post,Comment
from django.contrib.auth import logout
from django.http import JsonResponse

from django.core.paginator import Paginator






# Create your views here.
@login_required(login_url='/login/') 
def home(request):

    return render(request,'index.html')

def signup(request):
    
    if request.method == 'POST':
        # Get user input from the form
        username = request.POST['username']
        
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('singup')
        else:
            user = User.objects.create_user(username=username, password=password)

            if user:
                return redirect('login')  # Redirect to your logiin page
    return render(request,'sign.html')

def loginn(request):
    
    if request.method == 'POST':
        # Get user input from the form
        username = request.POST['username']
        
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')  # Redirect to your home page 
        else:
            messages.error(request, "Invalid username or password.")


    return render(request,'login.html')





@login_required(login_url='/login/') 
def create(request):
    if request.method == 'POST':
        # Get user input from the form
        titlle = request.POST['title']
        content = request.POST['content']
        usr=request.user
        if titlle and content is not None:
            save=Post(user=usr,title=titlle,content=content)
            save.save()
            return redirect('alllist')
    
    return render(request,'create.html')



def alllist(request):
    obj = Post.objects.all()
    paginator = Paginator(obj, 3)  # Show 5 items per page (you can adjust this number)

    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

    context = {
        'items': items,
    }
    return render(request, 'list.html', context)

def yourlist(request):
    obj = Post.objects.filter(user=request.user)
    paginator = Paginator(obj, 3)  # Show 5 items per page (you can adjust this number)

    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

    context = {
        'items': items,
    }
    return render(request, 'yourlist.html', context)



def viewbyid(request,id):
    post = get_object_or_404(Post, pk=id)  
    comments = Comment.objects.filter(post=post)
    c=comments.count()

    # when you have multiple form  in single view

    if request.method == 'POST':
            if "emails" in request.POST:
                recipient_email = request.POST.get('recipient_email')
                return redirect(f"mailto:{recipient_email}")

      

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            comment = Comment(content=content, author=request.user, post=post)
            comment.save()
            return redirect('viewbyid', id=post.id) 

    return render(request, 'full.html',{'post':post,'comments':comments,'c':c})
        



@login_required(login_url='/login/')       
def logoutt(request):
        
        logout(request)
        return redirect('login')
    



# views.py
from django.views.decorators.http import require_POST
import json


@login_required(login_url='/login/')   
def like_comment(request, id):
    print("hi")
    comment = get_object_or_404(Comment, id=id)
    user = request.user
    print("newww")

    if user in comment.likes.all():
        comment.likes.remove(user)
        liked = False
    else:
        comment.likes.add(user)
        liked = True
    
    response_data = {
        'liked': liked,
        'likes_count': comment.likes.count,
    }

    j=json.dumps(response_data)

    return JsonResponse(j)  


def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        return redirect(f"mailto:{recipient_email}")

    return redirect('email_input')