<%inherit file="base.mako" />
<!DOCTYPE html>
<html>
  <head>
    ${self.head()}
  </head>
  <body>
    ${self.header()}
    ${next.body()}
    <footer>
      ${self.footer()}
    </footer>
  </body>
</html>
<%def name="head()">
  <%include file="head.mako" />
</%def>
<%def name="header()">
  <%include file="header.mako" />
</%def>
<%def name="footer()">
  <%include file="footer.mako" />
</%def>
