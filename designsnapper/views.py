import random
from urlparse import urlparse

from django.core.cache import cache
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.template import RequestContext

from designsnapper.handlers import Client
from designsnapper.forms import CreateGreetingForm
from designsnapper.models import Greeting

MEMCACHE_GREETINGS = 'greetings'

def client(func):
    def add_client(self, *args):
        #self.account_id = 1

        #self.current_user = int(self.account_id)
        #self.snapper = Client(self.current_user)

        return func(self, *args)
        
    return add_client

@client
def debug(request):
    context = RequestContext(request)
    context['request'] = request
    context['snapper'] = request.snapper

    return render_to_response('debug.html', context, mimetype="application/json")

@client
def home(request):
    snapshots = range(10)
    return direct_to_template(request, 'index.html', {'snapshots': snapshots,})

@client
def settings(request):
    """View a list of all the pages you're currently monitoring"""
    
    pages = [{
        'url': 'http://www.apple.com',
        'guid': 'abcdefg',
        'status': random.randint(0,1),
        'screenshots': random.randint(1,3000)
        }, {
        'url': 'http://www.woothemes.com/',
        'guid': 'abcdefg',
        'status': random.randint(0,1),
        'screenshots': random.randint(1,3000)
        }, {
        'url': 'http://postmarkapp.com/',
        'guid': 'abcdefg',
        'status': random.randint(0,1),
        'screenshots': random.randint(1,3000)
        }, {
        'url': 'http://carbonmade.com/',
        'guid': 'abcdefg',
        'status': random.randint(0,1),
        'screenshots': random.randint(1,3000)
        }]

    return direct_to_template(request, 'settings.html', {'pages': pages,})

@client
def page(request):
    url = urlparse('http://www.turningart.com/')
    clean_url = "%s%s" % (url.netloc, url.path)

    """Dive into the history of an individual URL resource"""

    screenshots = range(10)
    
    layout = {
        'width': len(screenshots) * 445 + 300
    }

    page = {
        'url': url,
        'name': clean_url,
        'guid': 'abcdefg',
        'status': random.randint(0,1),
        'screenshots': screenshots
        }

    return direct_to_template(request, 'page.html', {'page': page, 'layout': layout})

@client
def add_pages(request):
    """Accept a list of web resources as URLs to monitor"""
    
    pass


def create_greeting(request):
    if request.method == 'POST':
        form = CreateGreetingForm(request.POST)
        if form.is_valid():
            greeting = form.save(commit=False)
            if request.user.is_authenticated():
                greeting.author = request.user
            greeting.save()
            cache.delete(MEMCACHE_GREETINGS)
    return HttpResponseRedirect('/designsnapper/')

def create_new_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user must be active for login to work
            user.is_active = True
            user.save()
            return HttpResponseRedirect('/designsnapper/')
    else:
        form = UserCreationForm()
    return direct_to_template(request, 'user_create_form.html',
        {'form': form})
