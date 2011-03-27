<%page args="post, detail=True"/>
<article class="hentry">
  <abbr class="updated" title="${ post.date.isoformat() }">
    ${post.date.strftime("%Y-%m-%d")}
  </abbr>
  <h2>
    <a href="${post.permapath()}" rel="bookmark" title="Permanent Link to ${post.title}">${post.title}</a>
  </h2>

% if detail:
  <ul class="tags">
% for category in post.categories:
    <li>
      <a href="${ category.path }" rel="tag" >${ category.name }</a>
    </li>
% endfor
  </ul>
  <div class="entry-content">
    ${self.post_prose(post)}
  </div>
% endif
</article>

<%def name="post_prose(post)">
  ${post.content}
</%def>
