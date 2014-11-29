#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PATH='content'

AUTHOR = u'Daniel Zappala'
BIO = u''
TAGLINE = u''
SITENAME = u'Finding My Family'
SITESUB = u'Zappala and Campbell Genealogy'
SITEURL = 'http://genealogy.zappala.org'

# Contact info
EMAIL = 'dzappala@cedarhills.org'
FACEBOOK_URL = 'https://www.facebook.com/daniel.zappala'

LICENSE = '<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>'

TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'

# Tag cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# How to save pages
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
SURNAME_URL = '{slug}'
SURNAME_SAVE_AS = '/surnames/{slug}.html'
PERSON_URL = '{slug}'
PERSON_SAVE_AS = '/people/{slug}.html'
INDEX_SAVE_AS = 'blog.html'

# Templates
DIRECT_TEMPLATES = ('index', 'tags', 'archives', 'surnames', 'people')


# Feeds
FEED_DOMAIN = SITEURL
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'

# Misc
STATIC_PATHS = ['images','docs']
DEFAULT_PAGINATION = 10

# Theme
USER_LOGO_URL = "/images/home/zappala-kids-easter-1973.jpg"
THEME = "themes/pelican-etna"

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors', 'summary', 'pelican-genealogy']

# Comments
# DISQUS_SITENAME = 'zappalagenealogy'

# For development only
RELATIVE_URLS = True
