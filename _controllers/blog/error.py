from blogofile.cache import bf

blog = bf.config.controllers.blog


def run():
    write_404()

def write_404(template="404.mako"):
    path = bf.util.path_join(blog.path, "404.html")
    blog.logger.info("Writing 404 page: " + path)
    bf.writer.materialize_template(template, path, {})
