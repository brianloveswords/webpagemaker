import re

import bleach
import html5lib

ALLOWED_TAGS = [
    "!doctype", "html", "body", "a", "abbr", "address", "area", "article",
    "aside", "audio", "b", "base", "bdi", "bdo", "blockquote", "body", "br",
    "button", "canvas", "caption", "cite", "code", "col", "colgroup",
    "command", "datalist", "dd", "del", "details", "dfn", "div", "dl", "dt",
    "em", "embed", "fieldset", "figcaption", "figure", "footer", "form",
    "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr",
    "html", "i", "iframe", "img", "input", "ins", "keygen", "kbd", "label",
    "legend", "li", "link", "map", "mark", "menu", "meta", "meter", "nav", 
    "noscript", "object", "ol", "optgroup", "option", "output", "p", "param",
    "pre", "progress", "q", "rp", "rt", "s", "samp", "section", "select",
    "small", "source", "span", "strong", "style", "sub", "summary", "sup", 
    "table", "tbody", "td", "textarea", "tfoot", "th", "thead", "time",
    "title", "tr", "track", "u", "ul", "var", "video", "wbr"
    ]

ALLOWED_ATTRS = {
    # TODO: We should probably add to this. What meta attributes can't
    # be abused for SEO purposes?
    "meta": ["charset", "name", "content"],
    "*": ["class", "id"],
    "img": ["src", "width", "height"],
    "a": ["href"],
    "base": ["href"],
    "iframe": ["src", "width", "height", "frameborder", "allowfullscreen"],
    "link": ["href", "rel", "type"],
    "object": ["height", "width"],
    "param": ["name", "value"],
    "embed": ["src", "type", "width", "height", "allowfullscreen", "allowscriptaccess", "flashvars"]
}

if bleach.VERSION < (1, 1, 1):
    raise Exception("Please use simon wex's bleach fork for now: " +
                    "https://github.com/simonwex/bleach.git")

def _comment_sanitizing_stream(stream):
    for item in stream:
        if item['type'] == "Comment":
            item['data'] = item['data'].replace('[', '{').replace(']', '}')
        yield item

def sanitize_comments(html):
    treebuilder = html5lib.treebuilders.getTreeBuilder("dom")
    parser = html5lib.HTMLParser(tree=treebuilder)
    walker = html5lib.treewalkers.getTreeWalker("dom")
    dom_tree = parser.parse(html)
    stream = walker(dom_tree)
    HTMLSerializer = html5lib.serializer.htmlserializer.HTMLSerializer
    s = HTMLSerializer(omit_optional_tags=False, quote_attr_values=True)
    return s.render(_comment_sanitizing_stream(stream))

def sanitize(html):
    html = bleach.clean(html, strip=True, strip_comments=False,
                        tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS,
                        parse_as_fragment=False)
    
    html = sanitize_comments(html)
    
    # We specifically want to check for an html5 doctype and start with one
    # if it's either missing or any other doctype.
    if not re.match(r'^\s*<!DOCTYPE html>', html, re.IGNORECASE):
        html = '<!DOCTYPE html>' + html
    
    return html
