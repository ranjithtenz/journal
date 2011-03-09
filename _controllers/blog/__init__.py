import logging

from blogofile.cache import bf

import categories
import chronological
import feed
import permapage
import post
import error

config = {
        "name": "Blog",
        "description": "Creates a Blog",
        "priority": 90.0,

        #Posts
        "post.date_format": "%Y/%m/%d %H:%M:%S"
        }

def run():
    blog = bf.config.controllers.blog

    #Parse the posts
    blog.posts = post.parse_posts("_posts")
    blog.dir = bf.util.path_join(bf.writer.output_dir, blog.path)

    blog.categorized_posts = {} ## "Category Name" -> [post, post, ... ]
    blog.all_categories = [] ## [("Category 1",num_in_category_1), ...] (sorted alphabetically)
    categories.sort_into_categories()

    blog.logger = logging.getLogger(config['name'])
    
    permapage.run()
    chronological.run()
    categories.run()
    feed.run()
    error.run()
