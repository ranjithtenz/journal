# -*- coding: utf-8 -*-
from blogofile import cache

site.url = "http://journal.uggedal.com"

#### Blog Settings ####
blog = controllers.blog

blog.enabled = True
blog.path = ""

blog.author = cache.HierarchicalCache()
blog.author.name = "Eivind Uggedal"
blog.author.email = "eivind@uggedal.com"
blog.author.url = "http://uggedal.com/"
blog.author.elsewhere = [
    ('@uggedal', 'http://twitter.com/uggedal/'),
    ('Was it up?', 'http://wasitup.com/'),
    ('Media Queries', 'http://mediaqueri.es/'),
]

blog.name = "Journal of %s" % blog.author.name
blog.description = blog.name

blog.analytics_key = "UA-1857692-3"

blog.timezone = "Europe/Oslo"
blog.posts_per_page = 1000
blog.auto_permalink.path = ":blog_path/:title"

blog.post_excerpts.enabled = False

blog.post_default_filters = {"markdown": "markdown, syntax_highlight, smartypants",}

blog.category_dir = "tags"

#### Filter Settings ####
filters.syntax_highlight.style = "trac"
filters.syntax_highlight.preload_styles = ["trac"]
filters.syntax_highlight.css_dir = ""
