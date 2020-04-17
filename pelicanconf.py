#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Iván Hernández Cazorla'
SITENAME = 'Coruja Digital'
SUBTITLE = 'Tecnologías de la información y la comunicación para el patrimonio y la ciencia abierta'
SITEURL = ''

PATH = 'content'

THEME = "theme"

TIMEZONE = 'Europe/London'

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

AWARN = ("<p>¡Estamos desarrollando el sitio web! Esperamos tenerlo lo"
        " más pronto posible.</p>"
        "<p>Para cualquier duda, proyecto o trabajo puedes contactar"
        " con nosotros en <a href='mailto:ivan@corujadigital.tech'>"
        "ivan@corujadigital.tech</a></p>")

TILE_ONE = {"title": "Qué hacemos",
            "slug": "servicios",
            "css_class": "is-primary",
            "content":
            "Patrimonio cultural<br>Humanidades digitales<br>Conocimiento libre</br>Ciencia abierta<br>Tecnología"}
TILE_TWO = {"title": "Contactar",
            "slug": "contactar",
            "css_class": "is-warning",
            "content":
            "<a href='mailto:info@corujadigital.com'>info@corujadigital.com</a>"}
TILE_THREE = {"title": "Clientes",
              "slug": "clientes",
              "image": "https://bulma.io/images/placeholders/640x480.png",
              "css_class": "is-info",
              "content": ""}
TILE_FOUR = {"title": "Quiénes somos",
             "slug": "acerca_de",
             "css_class": "is-link",
             "content":
             "Cat ipsum dolor sit amet, instantly break out into full speed gallop across the house for no reason so plop down in the middle where everybody walks."}

FOOTER = ("El contenido del sitio web está bajo"
          " <a href='https://creativecommons.org/licenses/by-sa/4.0/deed.es'>"
          "Creative Commons BY-SA 4.0</a>.")
