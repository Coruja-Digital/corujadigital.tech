#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Iván Hernández Cazorla'
SITENAME = 'Coruja Digital'
SUBTITLE = 'Tecnologías de la información y la comunicación para el patrimonio y la ciencia abierta'
SITEURL = 'https://corujadigital.tech'

PATH = 'content'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
STATIC_PATHS = ["documentos"]

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

TILE_ONE = {"title": "Qué hacemos",
            "slug": "servicios.html",
            "css_class": "is-primary",
            "content":
            "Patrimonio cultural<br>Humanidades digitales<br>Conocimiento libre</br>Ciencia abierta<br>Tecnología"}
TILE_TWO = {"title": "Contactar",
            "slug": "contactar.html",
            "css_class": "is-warning",
            "content":
            "¿Tienes alguna idea o propuesta que trasladarnos? ¿Estás interesado en alguno de nuestros servicios?"}
TILE_THREE = {"title": "Clientes",
              "slug": "clientes.html",
              "image": "theme/clientes.jpg",
              "css_class": "is-info",
              "content": ""}
TILE_FOUR = {"title": "Quiénes somos",
             "slug": "acerca-de.html",
             "css_class": "is-link",
             "content":
             "Somos un equipo multidisciplinar que ofrece diferentes servicios relacionados con las tecnologías de la información, la gestión, la comunicación y la difusión del patrimonio cultural, las humanidades digitales y la ciencia abierta."}

FOOTER = ("<a href='/creditos.html'>Créditos</a> del software y elementos gráficos utilizados.<br>"
          "El contenido del sitio web está bajo una licencia"
          " <a href='https://creativecommons.org/licenses/by-sa/4.0/deed.es'>"
          "Creative Commons BY-SA 4.0</a>.")
