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
        "markdown": "syntax_highlight, markdown",
}
blog.category_dir = "tags"
