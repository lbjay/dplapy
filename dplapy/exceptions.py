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

# exceptions.py - API-specific exceptions

__version__ = '0.1'

class APIException(Exception):
    """
    base exception class for the API
    """

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class APIHttpException(APIException):
    """
    indicates the api request return a non-200 http status
    """
    pass

class APIRequestException(APIException):
    """
    indicates the api response contained errors
    """
    pass

class APIInvalidSortException(Exception):
    """
    indicates the sort arguments were invalid
    """
    pass

class APIInvalidFacetException(Exception):
    """
    indicates the facet arguments were invalid
    """
    pass
