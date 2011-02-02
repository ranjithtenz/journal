import re
import os

import pygments
from pygments import util, formatters, lexers, highlight


css_files_written = set()

code_block_re = re.compile(
    r"<pre><code>"
    r"(?:#\!(?P<lang>\w+)\n)?"
    r"(?P<code>.*?)\n"
    r"</code></pre>", re.DOTALL
)


def highlight_code(code, language, formatter):
    try:
        lexer = pygments.lexers.get_lexer_by_name(language)
    except pygments.util.ClassNotFound:
        lexer = pygments.lexers.get_lexer_by_name("text")
    #Highlight with pygments and surround by blank lines
    #(blank lines required for markdown syntax)
    highlighted = "\n\n{0}\n\n".format(
            pygments.highlight(code, lexer, formatter))
    return highlighted


def write_pygments_css(style, formatter):
    import blogofile_bf as bf

    location=bf.config.filters.syntax_highlight.css_dir
    path = bf.util.path_join("_site", bf.util.fs_site_path_helper(location))
    bf.util.mkdir(path)
    css_file = "pygments_{0}.css".format(style)
    css_path = os.path.join(path, css_file)
    css_site_path = css_path.replace("_site", "")
    if css_site_path in css_files_written:
        return #already written, no need to overwrite it.
    f = open(css_path, "w")
    css_class = ".pygments_{0}".format(style)
    f.write(formatter.get_style_defs(css_class))
    f.close()
    css_files_written.add(css_site_path)

from mako.filters import html_entities_unescape

def run(src):
    import blogofile_bf as bf

    style = bf.config.filters.syntax_highlight.style
    css_class = "pygments_"+style
    formatter = formatters.HtmlFormatter(
            linenos=False, cssclass=css_class, style=style)
    write_pygments_css(style, formatter)

    def repl(m):
        lang = m.group('lang')
        code = m.group('code')

        code = html_entities_unescape(code)

        return highlight_code(code,lang,formatter)

    return code_block_re.sub(repl, src)
