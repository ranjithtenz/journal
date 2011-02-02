<%inherit file="base.mako" />
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<html>
  <head>
    ${self.head()}
  </head>
  <body>
    ${self.header()}
    ${next.body()}
    <p id="elsewhere">
      TODO
    </p>
    <p id="footer">
      ${self.footer()}
    </p>
  </body>
  <script type='text/javascript'>
    var gaJsHost = (("https:" == document.location.protocol) ?
                   "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost +
                            "google-analytics.com/ga.js' type='text/" +
                            "javascript'%3E%3C/script%3E"));
  </script>
  <script type='text/javascript'>
    var pageTracker = _gat._getTracker("TODO");
    pageTracker._initData();
    pageTracker._trackPageview();
  </script>
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
