from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from managers import *

class BaseHandler(webapp.RequestHandler):
  def render(self, template_file, template_values, **kwargs):
    template_path = 'templates/%s' % template_file  

class ManageHandler(BaseHandler):
  return
  
class PageAddHandler(BaseHandler):
  return
  
class PageRemoveHandler(BaseHandler):
  return