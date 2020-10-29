#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Iván Hernández Cazorla'
SITENAME = 'Coruja Digital'
SUBTITLE = 'Tecnologías de la información y la comunicación para el patrimonio y la ciencia abierta'
SITEURL = 'https://corujadigital.tech'

ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}'
PATH = 'content'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAG_URL = 'blog/tag/{slug}'
STATIC_PATHS = ["documentos"]
TEMPLATE_PAGES = {'blog.html': 'blog.html'}

# Don't generate specific templates
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

THEME = "theme"

TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = "%d de %B de %Y"

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

WARN = ("<p>¡Estamos desarrollando el sitio web! Esperamos tenerlo lo"
        " más pronto posible.</p>"
        "<p>Para cualquier duda, proyecto o trabajo puedes contactar"
        " con nosotros en <a href='mailto:ivan@corujadigital.tech'>"
        " ivan@corujadigital.tech</a></p>")

CARD_ONE = {"title": "Qué hacemos",
            "slug": "servicios",
            "css_class": "is-primary",
            "more": "Conoce nuestros servicios",
            "content":
            "<div class='tags are-large is-centered m-2'>"
            "<span class='tag'>Patrimonio cultural</span>"
            "<span class='tag'>Humanidades digitales</span>"
            "<span class='tag'>Conocimiento libre</span>"
            "<span class='tag'>Ciencia abierta</span>"
            "<span class='tag'>Tecnología</span>"
            "<span class='tag'>MediaWiki</span>"
            "<span class='tag'>Semantic MediaWiki</span>"
            "<span class='tag'>Wikibase</span></div>"}
CARD_TWO = {"title": "Contactar",
            "slug": "contactar",
            "css_class": "is-warning",
            "more": "Contactar",
            "content":
            "¿Tienes alguna idea o propuesta que trasladarnos? ¿Estás interesado en alguno de nuestros servicios?"}
CARD_THREE = {"title": "Clientes",
              "slug": "clientes",
              "image": "theme/clientes.jpg",
              "more": "Conoce los proyectos que hemos realizado",
              "css_class": "is-info",
              "content": ""}
CARD_FOUR = {"title": "Quiénes somos",
             "slug": "acerca-de",
             "css_class": "is-link",
             "more": "Leer más",
             "content":
             "Somos un equipo multidisciplinar que ofrece diferentes servicios relacionados con las tecnologías de la información, la gestión, la comunicación y la difusión del patrimonio cultural, las humanidades digitales y la ciencia abierta."}

CARD_FIVE = {"title": "Recursos liberados",
             "slug": "recursos_liberados",
             "css_class": "is-link",
             "more": "Accede a nuestros recursos",
             "content":
             "Creemos en el conocimiento y el software libre,"
             " por ello liberamos gran parte del contenido que producimos,"
             " desde presentaciones a programas. Además, incentivamos a"
             " nuestros clientes a unirse a esta iniciativa."}

FOOTER = ("<a href='/creditos'>Créditos</a> del software y elementos gráficos utilizados.<br>"
          "El contenido del sitio web está bajo una licencia"
          " <a href='https://creativecommons.org/licenses/by-sa/4.0/deed.es'>"
          "Creative Commons BY-SA 4.0</a>.<br>"
          "<a href='/aviso-legal'>Aviso legal</a><br>"
          "<a href='/politica-privacidad'>Política de privacidad</a>")

NAVBARMAIN = (("Inicio", "https://corujadigital.tech"),
              ("Quiénes somos", "/acerca-de"),
              ("Servicios", "/servicios"),
              ("Clientes", "/clientes"),
              ("Blog", "/blog"),
              ("Recursos liberados", "/recursos-liberados"),
              ("Contactar", "/contactar"))

PLUGINS = ["pelican.plugins.seo", "pelican.plugins.sitemap"]

SITEMAP = {
    "format": "xml",
    "priorities": {
        "article": 0.8,
        "pages": 0.8,
        "indexes": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "pages": "monthly",
        "indexes": "daily"
    }
}

SEO_REPORT = True
SEO_ENHANCER = False

LOGO = "https://corujadigital.tech/theme/logo_coruja_digital.png"
