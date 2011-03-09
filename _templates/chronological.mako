<%inherit file="site.mako" />
% for post in posts:
  <%include file="post.mako" args="post=post" />
% endfor
% if prev_link or next_link:
  <p id="pagination">
  % if prev_link:
    <a href="${prev_link}">&laquo; Previous Page</a>
  % endif
  % if prev_link and next_link:
    &mdash;
  % endif
  % if next_link:
    <a href="${next_link}">Next Page &raquo;</a>
  % endif
  </p>
% endif
