<header>
  <h1>
    <a href="${bf.util.site_path_helper()}">${bf.config.blog.name}</a>
  </h1>
  <p id="elsewhere">
% for service, url in bf.config.blog.author.elsewhere:
    <a href="${ url }">${ service }</a>
% endfor
  </p>
</header>
