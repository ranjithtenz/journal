<%inherit file="site.mako" />
% for i, post in enumerate(posts):
  <%include file="post.mako" args="post=post, detail=i==0" />
% endfor
