# -*- coding: utf-8 -*-
AUTHOR = u'Marcel Hellkamp'
SITENAME = u"goe.py"
SITESUBTITLE = u"Python User Group Göttingen"
SITEURL = 'http://goepy.de/blog'
TIMEZONE = "Europe/Berlin"
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_ORPHANS = 3
DEFAULT_PAGINATION = 10

GITHUB_URL = 'http://github.com/defnull/goepy.de'

#MENUITEMS = (('Home','/blog'),)

LINKS = (
  ('python.org','http://python.org/'),
  ('Deutsches Python Forum','http://python-forum.de/'),
  ('Python Wiki','http://wiki.python.de'),
  ('Python Stammtisch Hannover','http://www.python-hannover.de'),
)
      

#SOCIAL = (('twitter', 'http://twitter.com/bottlepy'),
#          ('github', 'http://github.com/defnull'),)

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["static", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('static/robots.txt', 'robots.txt'),
                 ('static/favicon.ico', 'favicon.ico'),)

