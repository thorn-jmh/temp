The pipeline of scrapy in **html_content_pipelines.py** that **cleans HTML content** in following steps:

Removes any <meta> tags

Removes any embedded objects (flash, iframes)

Removes any <link> tags

Removes any style tags

Removes any processing instructions

Removes any style attributes. Defaults to the value of the style option

Removes any Javascript, like an onclick attribute. Also removes stylesheets as they could contain Javascript

Removes any comments

Removes any frame-related tags

Removes any form tags

Tags that aren't wrong, but are annoying. <blink> and <marquee>

Remove any tags that aren't standard parts of HTML

Keep src, color, href, title, name attrs only

Remove span, font, div tags. Their content will get pulled up into the parent tag

