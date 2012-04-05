DESCRIPTION
-----------

dplapy is a python module that provices a wrapper to the DPLA API

INSTALLATION
------------

If you prefer, you can check out the latest version of the source using
Git:

    git clone https://github.com/lbjay/dplapy.git
    
To install:

    python setup.py install

EXAMPLE USAGE
-------------

    import dplapy
    api = dplapy.APIConnection('http://api.dp.la/dev/item/')

    resp = api.query('biography')
    
-or-

    resp = api.query('turtles', sort=('checkouts', dplapy.DESCENDING))
    
-or-

    resp = api.title_query('germany', facet=['creator','subject'])
    
-or-

    resp = api.subject_query('agriculture', limit=1, start=34356)

TODO
----

- add .next_page() and .prev_page() methods to response object
- allow facets="all"

LICENSE
-------

GPL/BSD (Dual Licensed), portions under the Apache License

AUTHORS
-------

Jay Luker <lbjay@reallywow.com>
