<title>${bf.config.blog.name}</title>
% if category:
  <link rel="alternate" type="application/atom+xml" title="Atom 1.0"
        href="${bf.util.site_path_helper(bf.config.blog.path, bf.config.blog.category_dir, "%s.atom" % category.url_name)}">
% else:
  <link rel="alternate" type="application/atom+xml" title="Atom 1.0"
        href="${bf.util.site_path_helper(bf.config.blog.path, 'index.atom')}">
% endif
<link rel='stylesheet' type='text/css' href='/style.css'>
<link rel='stylesheet' type='text/css'
  href='${bf.config.filters.syntax_highlight.css_dir}/pygments_${bf.config.filters.syntax_highlight.style}.css'>
