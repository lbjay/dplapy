# Copyright (C) 2012 Jay Luker
#
# This file is part of dplapy, the Python DPLA API module.
#
# dplapy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dplapy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dplapy.  If not, see <http://www.gnu.org/licenses/>.

# api.py - core API module

__version__ = '0.1'

import urlparse
import httplib2
import urllib
import urllib2
import simplejson

class APIConnection(object):
    """
    Represents a DPLA API endpoint
    """

    def __init__(self, url, cache=None, timeout=None):
        """     
        url -- URI pointing to the API instance. Examples:

            http://api.dp.la/dev/item

        cache -- cache value to init the http connection with
            If 'cache' is a string then it is used as a directory name
            for a disk cache. Otherwise it must be an object that supports
            the same interface as FileCache.

        timeout -- Timeout, in seconds, for the server to response.
            By default, use the python default timeout (of none?)

        """   
        self.scheme, self.host, self.path = urlparse.urlparse(url, 'http')[:3]
        assert self.scheme in ('http','https')

        self.url = url
        self.http = httplib2.Http(cache=cache, timeout=timeout)

    def query(self, q, type='keyword', **params):
        if q is not None:
            params['query'] = q
        params['search_type'] = type
        try:
            (r,c) = self.http.request(self.query_url(params))
        except:
            raise
        return APIResponse(c)

    def query_url(self, params):
        qstring = urllib.urlencode(params)
        return "%s?%s" % (self.url, qstring)
        
class APIResponse(object):
    """
    Represents the API search results
    """
    def __init__(self, content):
        self.raw = simplejson.loads(content)

    def is_error(self):
        return len(self.raw['errors']) > 0

    def count(self):
        return self.raw['num_found']

    def facets(self, fields=[]):
        if type(self.raw['facets']) is not dict:
            return {}
        if len(fields):
            return dict((k,v) for k,v in self.raw['facets'].items() if k in fields)
        return self.raw['facets']
            
