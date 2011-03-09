from blogofile.cache import bf

blog = bf.config.controllers.blog


def run():
    write_feed(blog.posts, bf.util.path_join(blog.path), "index.atom")

def write_feed(posts, root, filename, template="atom.mako"):
    root = root.lstrip("/")
    path = bf.util.path_join(root, filename)
    blog.logger.info("Writing Atom feed: " + path)
    env = {"posts": posts, "root": root}
    bf.writer.materialize_template(template, path, env)
