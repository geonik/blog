#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'George Nikolopoulos'
SITENAME = u'Programming, Philosophy and stuff'
SITEURL = 'http://geonik.github.io'
THEME = '/home/george/repos/pelican-themes/pelican-bootstrap3'

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_MAX_ITEMS = 10

BOOTSTRAP_THEME = 'paper'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
