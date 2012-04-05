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

import sys
import urlparse
import httplib2
import urllib
from response import APIResponse
from exceptions import *
#from paginator import APIPaginator

ASCENDING = 'asc'
DESCENDING = 'desc'

class APIConnection(object):
    """
    Represents a DPLA API endpoint
    """

    def __init__(self, url, cache=None, timeout=None, debug=False):
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

        self.debug = debug
        self.url = url
        self.http = httplib2.Http(cache=cache, timeout=timeout)

    def query(self, q, sort=None, facet=None, search_type='keyword', **params):

        if q is not None:
            params['query'] = q
        params['search_type'] = search_type

        if sort:
            try:
                assert type(sort) is tuple
                assert len(sort) == 2
                assert sort[1] in (ASCENDING, DESCENDING)                
            except AssertionError:
                msg = "sort must be a tuple containing field name " \
                    + "plus one of dplapy.ASCENDING or dplapy.DESCENDING"
                raise APIInvalidSortException(msg)
            params['sort'] = "%s %s" % sort

        if facet:
            try:
                assert type(facet) is list
            except AssertionError, e:
                raise APIInvalidFacetException("facet must be a list of field names")                
            params.setdefault('facet', [])
            for field in facet:
                params['facet'].append(field)

        request_url = self.query_url(params)
        if self.debug:
            print >>sys.stderr, "request url: " + request_url

        (headers,content) = self.http.request(request_url)

        resp = APIResponse(headers,content)

        if resp.is_error():
            raise APIRequestException(resp.errors)
        elif not resp.http_ok():
            raise APIHttpException("http status: " + resp.status())

        return resp

    def title_query(self, *args, **kwargs):
        kwargs['search_type'] = 'title_keyword'
        return self.query(*args, **kwargs)

    def desc_query(self, *args, **kwargs):
        kwargs['search_type'] = 'desc_keyword'
        return self.query(*args, **kwargs)

    def creator_query(self, *args, **kwargs):
        kwargs['search_type'] = 'creator_keyword'
        return self.query(*args, **kwargs)

    def subject_query(self, *args, **kwargs):
        kwargs['search_type'] = 'subject_keyword'
        return self.query(*args, **kwargs)

    def query_url(self, params):
        qstring = urllib.urlencode(params, doseq=True)
        return "%s?%s" % (self.url, qstring)
        
