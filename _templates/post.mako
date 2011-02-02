<%page args="post"/>
<div class="hentry">
  <abbr class="updated" title="${ post.date.isoformat() }">
    ${post.date.strftime("%Y-%m-%d")}
  </abbr>
  <h2>
    <a href="${post.permapath()}" rel="bookmark" title="Permanent Link to ${post.title}">${post.title}</a>
  </h2>
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
</div>

<%def name="post_prose(post)">
  ${post.content}
</%def>
