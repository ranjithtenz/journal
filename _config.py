# -*- coding: utf-8 -*-

site.url = "http://journal.uggedal.com"

#### Blog Settings ####
blog = controllers.blog

blog.enabled = True
blog.path = ""
blog.name = "Journal of Eivind Uggedal"
blog.description = blog.name
blog.timezone = "Europe/Oslo"
blog.posts_per_page = 10
blog.auto_permalink.path = ":blog_path/:title"
blog.post_excerpts.enabled = False
blog.post_default_filters = {
        "markdown": "markdown, syntax_highlight",
}
blog.category_dir = "tags"

#### Filter Settings ####
filters.syntax_highlight.style = "trac"
filters.syntax_highlight.preload_styles = ["trac"]
filters.syntax_highlight.css_dir = ""
