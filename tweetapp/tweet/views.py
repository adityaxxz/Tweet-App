from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm, SearchForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'index.html')


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required     #this is a decorator that checks if the user is logged in, if not it redirects to the login page
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm()
    
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form=TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid(): 
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form=TweetForm(instance=tweet)

    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet=get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def tweet_search(request):
    search_results = []
    form = SearchForm()
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_results = Tweet.objects.filter(text__icontains=query).order_by('-created_at')

    return render(request, 'tweet_search.html', {
        'form': form,
        'search_results': search_results,
        'search_performed': 'query' in request.GET
    })


@csrf_exempt
def custom_logout(request):
    """
    Custom logout view that handles both GET and POST requests.
    The CSRF exemption allows it to work without a CSRF token.
    """
    # Django's auth logout function
    logout(request)
    
    # Redirect to the tweet list page
    return redirect('tweet_list')