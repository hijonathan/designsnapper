import re
import hmac
import base64
import httplib
import logging

import urllib2

import BeautifulSoup as soup

try:
    import hashlib
except ImportError:
    import md5 as hashlib

try:
    import json as simplejson
    simplejson.loads
except (ImportError, AttributeError):
    try:
        import simplejson
        simplejson.loads
    except (ImportError, AttributeError):
        try:
            from django.utils import simplejson
            simplejson.loads
        except (ImportError, AttributeError):
            try:
                import jsonlib as simplejson
                simplejson.loads
            except:
                pass

class BaseClient(object):
    """Client for interacting with the APIs"""
    
    def _create_path(self, method):
        pass
    
    def _http_error(self, code, message, url):
        logging.error('Client request error. Code: %s - Reason: %s - URL: %s' % (str(code), message, url))
    
    def _prepare_response(self, code, data):
        msg = self._get_msg(code)
        return {'status': code, 'body': data, 'msg': msg}
    
    def _get_msg(self, code):
        return None
    
    def _make_request(self, method, params, data=None, request_method='GET', url=None, content_type='application/json'):
        
        if not url: url = '/%s?%s' %(
            self._create_path(method),
            urllib2.urlencode(params)
        )
        
        if data and not isinstance(data, str):
            data = urllib2.urlencode(data)
        
        headers = {'Content-Type': content_type}
        client.request(request_method, url, data, headers)
        result = client.getresponse()
        if result.status < 400:
            body = result.read()
            client.close()
            if body:
                return self._prepare_response(result.status, simplejson.loads(body))
            else:
                return self._prepare_response(result.status, {})
        else:
            client.close()
            self._http_error(result.status,
                result.reason,
                url
            )
            return self._prepare_response(result.status, {})

class Client(BaseClient):
    """Client for managing pages in the app"""

    def _create_path(self, method):
        return '/%s' % (method)

    def get_pages(self):
        return self._make_request('pages', {})

    def get_page(self, keyword_guid):
        return self._make_request('pages/%s' % page_guid, {})

    def add_page(self, page):
        data = []
        for p in page:
            if p != '':
                data.append(dict(page=str(k)))

        return self._make_request('pages', {}, data=str(data), request_method='PUT')

    def delete_page(self, page_guid):
        return self._make_request('pages/%s' % page_guid, {}, request_method='DELETE')

    def refresh_all_pages(self):
        return self._make_request('pages/*/refresh', {})

    def refresh_page(self, page_guid):
        return self._make_request('pages/%s/refresh' % page_guid, {})

class BaseClass(object):
    """Base client for setting defaults"""


class Page(BaseClass):
    """Handles fetching and displaying information for monitored pages""" 

    def get_title(self):
        page = soup(urllib2.urlopen('http://www.turningart.com'))
        
        return page.html.head.title

class Thumbalizr(BaseClass):
    """Handles logic and actions for getting snapshots"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    