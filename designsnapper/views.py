import random
from datetime import date
from urlparse import urlparse

from django.core.cache import cache
from django.contrib.auth.forms import UserCreationForm

from django.views.generic import View

from django.shortcuts import render_to_response
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.utils import simplejson
from django.template import RequestContext

from designsnapper.handlers import Client

def client(func):
    def add_client(self, *args):
        #self.account_id = 1

        #self.current_user = int(self.account_id)
        #self.snapper = Client(self.current_user)

        return func(self, *args)
        
    return add_client

class DebugView(View):
    """Simple page you can hit when debugging"""

    @client
    def get(self, request):
        context = RequestContext(request)
        context['request'] = request

        return render_to_response('debug.html', context, mimetype="application/json")


class HomeView(View):
    """Render the home page."""

    @client
    def get(self, request):
        context = RequestContext(request)
        
        snapshots = range(10)
        return render_to_response('index.html', {'snapshots': snapshots,}, context)


class ManageView(View):
    """Handles displaying/adding/removing pages you're monitoring."""

    @client
    def get(self, request):
        pages = get_all_pages(0001)

        return render_to_response('manage.html', {'pages': pages})


class PageView(View):
    """The historical profile of a specific page"""

    @client
    def get(self, request):
        """Dive into the history of an individual URL resource"""

        context = RequestContext(request)
        screenshots = range(10)
        screenshot_count = len(screenshots)
        guid = request.GET.get('url')
        # guid = 'apple'

        page = get_page_versions(guid)

        # page = {
        #     'url': url,
        #     'name': clean_url,
        #     'date': 'August 9, 2011',
        #     'guid': 'abcdefg',
        #     'status': random.randint(0,1),
        #     'screenshots': screenshots
        # }

        return render_to_response('page.html', {'page': page, 'screenshot_count': screenshot_count}, context)


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

@client
def add_pages(request):
    """Accept a list of URLs to monitor"""

    pass

@client
def remove_pages(request):
    """Accept a dictionary of URLs to stop monitoring"""

    pass

# Mock data

def get_all_pages(userId):
    """Get a list of pages being monitored by this account."""

    # TODO: Query the db for the user-specific data
    
    pages = [
        {
            'url': 'http://www.apple.com',
            'guid': 'apple',
            'status': random.randint(0,1),
            'screenshot': get_recent_screenshot('apple'),
            'screenshots': random.randint(1,3000)
        }, {
            'url': 'http://www.zendesk.com/',
            'guid': 'zendesk',
            'status': random.randint(0,1),
            'screenshot': get_recent_screenshot('zendesk'),
            'screenshots': random.randint(1,3000)
        }, {
            'url': 'http://www.turningart.com/',
            'guid': 'turningart',
            'status': random.randint(0,1),
            'screenshot': get_recent_screenshot('turningart'),
            'screenshots': random.randint(1,3000)
        }, {
            'url': 'http://www.wistia.com/',
            'guid': 'wistia',
            'status': random.randint(0,1),
            'screenshot': get_recent_screenshot('wistia'),
            'screenshots': random.randint(1,3000)
        }
    ]
    
    return pages

def get_page_versions(guid):
    """Returns a dictionary of version objects for the given page."""

    page = {}
    version = {}
    
    # TODO: Get actual data from the db

    url = urlparse('http://www.%s.com' % guid)
    clean_url = "%s%s" % (url.netloc, url.path)
    
    page['url'] = 'http://www.%s.com' % guid
    page['name'] = clean_url
    page['status'] = 200
    page['versions'] = []

    for i in range(10):

        version['date'] = 'August 9, 2011'
        version['guid'] = '0001'
        version['screenshot'] = {}
        version['screenshot']['path'] = '/static/screenshots/%s.png' % guid
        
        page['versions'].append(version)
    
    return page

def get_recent_screenshot(guid):
    """Get the most current screenshot we have on file."""

    # TODO: Query the db for the most-recent screenshot
    
    response = {
        'status': 200,
        'screenshot': {
            'path': '/static/screenshots/%s.png' % guid
        }
    }
    
    return response
