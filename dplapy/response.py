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

# response.py - API response class

__version__ = '0.1'

import simplejson

class APIResponse(object):
    """
    Represents the API search results
    """
    def __init__(self, headers, content):
        self.raw = simplejson.loads(content)
        self.headers = headers

    def status(self):
        return self.headers['status']

    def http_ok(self):
        return self.headers['status'] == '200'

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

    def results(self):
        return self.raw['docs']
            
