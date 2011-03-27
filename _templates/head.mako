<title>${bf.config.blog.name}</title>
% if category:
  <link rel="alternate" type="application/atom+xml" title="Atom 1.0"
        href="${bf.util.site_path_helper(bf.config.blog.path, bf.config.blog.category_dir, "%s.atom" % category.url_name)}">
% else:
  <link rel="alternate" type="application/atom+xml" title="Atom 1.0"
        href="${bf.util.site_path_helper(bf.config.blog.path, 'index.atom')}">
% endif
<!--[if lt IE 9]>
<script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
<![endif]-->
<link rel='stylesheet' type='text/css' href='/style.css'>
<link rel='stylesheet' type='text/css'
  href='${bf.config.filters.syntax_highlight.css_dir}/pygments_${bf.config.filters.syntax_highlight.style}.css'>

<script type="text/javascript">
  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '${ bf.config.blog.analytics_key }']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script');
    ga.type = 'text/javascript';
    ga.async = true;
    ga.src = 'http://www.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(ga, s);
  })();
</script>
