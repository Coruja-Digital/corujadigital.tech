Title: Wikidata-IATEXT 2020: proyecto de humanidades y ciencia abierta
Category: Ciencia abierta
Date: 2020-12-07
Description: ...
Slug: wikidata-iatext-2020-ciencia-abierta-libre
Tags: ciencia abierta, conocimiento libre, Wikidata, WikiCite, Scholia, WikiProject Source Metadata
Modified: 2020-12-07

Wikidata es una base de conocimiento libre con más de 90&nbsp;millones de elementos (datos consultados en la [página principal de Wikidata](https://wikidata.org) de Wikidata el 7 de diciembre de 2020). Cada elemento representa algo concreto: una persona, un objeto, un lugar, una máquina, un lenguaje, etc. Se puede decir entonces que Wikidata pretende almacenar cada pieza del conocimiento humano y enlazarlo entre sí.

Dentro del universo que supone Wikidata, tanto por su contenido como por su comunidad, se pueden crear wikiproyectos: grupos flexibles y abiertos en los que las personas interesadas se pueden involucrar para organizar y definir el conocimiento sobre un tema específico. Entre los wikiproyectos hay varios que se dedican a tratar Wikidata como un conjunto de datos bibliográficos, como el [*WikiProject Source Metadata*](https://www.wikidata.org/wiki/Wikidata:WikiProject_Source_MetaData), parte de WikiCite.

<figure class="image">
  <img src="/theme/images/wikicite_logo.png" alt="Logo de WikiCite, una llave abierta y otra cerrada seguida del nombre de la iniciativa en minúscula" />
  <figcaption>Logo de WikiCite, una iniciativa para favorecer el uso de Wikidata como un corpus de datos bibliográficos.</figcaption>
</figure>

[WikiCite](https://meta.wikimedia.org/wiki/WikiCite) es una iniciativa aún más amplia que el mencionado wikiproyecto. No solo actúa como una iniciativa comunitaria para desarrollar un *corpus* de datos bibliográficos y de citas abiertas, sino que también se organizan conferencias, talleres y se dan subvenciones. Todo esto con el objetivo de **ampliar y mejorar el conocimiento libre sobre la humanidad y enlazarlo entre sí**.

## Wikidata y la ciencia abierta

Este tipo de proyectos no solo benefician si tenemos en cuenta el amplio concepto de conocimiento libre (en inglés, *open knowledge*), sino que hacen una contribución directa a iniciativas basadas en el concepto de ciencia abierta: facilitar el acceso a la investigación científica, desde publicaciones hasta conjuntos de datos y software. Este concepto, que también se podría definir como movimiento, insiste también en que la difusión sea accesible por cualquier persona, ya sean investigadores o aficionados.

Proyectos como WikiCite y el *WikiProject Source Metadata* facilitan que Wikidata se utilice con el objetivo de facilitar el acceso a la ciencia. En 2018 Coruja Digital propuso al [Instituto Universitario de Análisis y Aplicaciones Textuales](https://iatext.ulpgc.es) (IATEXT) un proyecto con el que contribuir tanto a la ciencia abierta como a Wikidata, en el marco de la iniciativa WikiCite: el Wikidata-IATEXT.

## Wikidata-IATEXT: humanidades, ciencia abierta, Wikidata y WikiCite

El proyecto propuesto se denominó Wikidata-IATEXT y tuvo los siguientes objetivos:

1. Compilar datos sobre sus investigadores y sus respectivas publicaciones científicas.
2. Introducirlos los datos compilados en Wikidata.

El proyecto comenzó en febrero de 2018, cuando en Wikidata había alrededor de 4300 institutos de investigación ([Q31855](https://www.wikidata.org/wiki/Q31855)), 86 de ellos con al menos 1 investigador enlazado con la propiedad "miembro de" ([P463](https://www.wikidata.org/wiki/Property:P463)) y 25 institutos universitarios con al menos una publicación enlazada a uno de sus miembros.

El 20 de junio de 2019 publiqué una entrada en mi blog personal con el objetivo de difundir mi participación en los Wikidata Days 2019, un congreso al que fui invitado para presentar los resultados y conclusiones del proyecto Wikidata-IATEXT: "[Wikidata-IATEXT, WikICite y Scholia en los Wikidata Days 2019](https://ivanhercaz.com/a/wikidata-iatext_wikicite_scholia_corpus_datos_bibliogr%C3%A1ficos_wikidata.html)".

A finales de diciembre de 2019 se publicó el artículo *Wikidata, WikiCite y Scholia como herramientas para un corpus de datos bibliográficos enlazados. Curación y estructuración de la producción científica de los investigadores del IATEXT* en el número 40 de Prisma.com (*Revista de Ciências e Tecnologias da Informação e Comunicação*). Está coautorizado por Manuel Ramírez Sánchez, antiguo coordinador de la división de Patrimonio Documental y Bibliometría del IATEXT, y Gregorio Rodríguez Herrera, director de dicho instituto, y se puede [consultar en accedaCRIS](http://hdl.handle.net/10553/60056), el repositorio institucional de la Universidad de Las Palmas de Gran Canaria.

El artículo presenta científica y detalladamente el proyecto Wikidata-IATEXT: las oportunidades de contribuir a la ciencia abierta y cómo, el proyecto Wikidata-IATEXT, su motivación y estado previo, la metodología aplicada, los resultados obtenidos, posibles casos de uso y problemas que afrontar. Recomendamos su lectura para un análisis completo de los datos con los que se trabajó y el resto de cuestiones mencionadas.

También se creó un [repositorio de datos en GitHub](https://github.com/Coruja-Digital/wikidata-iatext) y en [Zenodo](http://doi.org/10.5281/zenodo.1461382) para facilitar la consulta de los mismos y del exportador utilizado, una herramienta que tenemos pendiente mejorar. El repositorio de Zenodo proporciona un DOI, en caso de que se quiera citar o de que se utilice el repositorio de datos: [10.5281/zenodo.1461382](http://doi.org/10.5281/zenodo.1461382)

## Wikidata-IATEXT 2020: introducción de nuevos datos

En 2020 el IATEXT ofreció a Coruja Digital realizar una revisión de las publicaciones de los investigadores, ya que en el paso de 2 años sus miembros habían publicado más obras (artículos, ponencias, capítulos de libros, libros, etc.).

La metodología utilizada fue similar a la de la primera edición de este proyecto, descrita en el artículo científico mencionado anteriormente. Sin embargo, en esta ocasión contamos con una fuente directa, [un listado de publicaciones](https://iatext.ulpgc.es/publicaciones) elaborado por el IATEXT, y pudimos utilizar y cotejar prácticamente todos los artículos con accedaCRIS. En la edición anterior también utilizamos este repositorio como fuente, pero no disponía de todos los artículos, por lo que la principal fuente fue [Dialnet](https://dialnet.unirioja.es), una base de datos bibliográfica gestionada por la Fundación Dialnet, de la Universidad de La Rioja. 

Además, quisimos comprobar que los elementos de los investigadores tuviesen un mínimo de propiedades concretas. Para ello elaboramos un esquema de entidad (en inglés, *Entity Schema*) para confirmar la integridad del modelo de datos de la edición anterior. El esquema en cuestión es el [E220](https://www.wikidata.org/wiki/EntitySchema:E220), "miembros del Instituto Universitario de Análisis y Aplicaciones Textuales".

El proyecto se planteó a 2-3 meses y conllevó 8&nbsp;315 ediciones, de las que 248 conllevan la creación de elementos.

### Miembros

En cuanto a los miembros, se añadieron 4 nuevos que no constaban anteriormente y se creó el esquema mencionado previamente. Los elementos creados son los referidos a Luis Alberto Anaya Hernández ([Q96243406](https://wikidata.org/wiki/Q96243406)), Jesús Alexis García Moreno ([Q96243322](https://wikidata.org/wiki/Q96243322)), Aarón Moisés Santana Cordero ([Q96243136](https://wikidata.org/wiki/Q96243136)) y José Manuel Rodríguez Herrera ([Q96241945](https://wikidata.org/wiki/Q96241945)).

### Publicaciones

Se crearon 244 elementos de publicaciones científicas de miembros del IATEXT o de sujetos relacionados con las mismas (revistas, actas, obras coordinadas, etc.). Estos sujetos relacionados son necesarios para crear elementos de publicaciones científicas que tengan un mínimo de completitud: debemos saber dónde se ha publicado la obra que representa el elemento. Si restamos este tipo de elementos, se obtiene la cifra de 205 elementos sobre publicaciones.

La creación de estos nuevos elementos también conllevó la revisión de elementos de la edición anterior, de manera que algunos se pudieron complementar con algunos aspectos adicionales, como es el caso de la adición de referencias entre elementos ya existentes gracias al uso de [Dialnet Métricas](https://dialnet.unirioja.es/metricas/) como fuente.

<iframe style="width: 80vw; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#%23defaultView%3ABarChart%0A%23%20Pages%20per%20year%20bar%20chart%20of%20an%20organization%0ASELECT%0A%20%20%3Fyear%0A%20%20(SUM(%3Fpages_per_author)%20AS%20%3Fnumber_of_pages)%0A%20%20%3Fresearcher_label%0AWHERE%20%7B%0A%20%20%7B%0A%20%20%20%20SELECT%0A%20%20%20%20%20%20%3Fresearcher_label%20%3Fwork%20%3Fyear%0A%20%20%20%20%20%20(SAMPLE(%3Fpages)%20%2F%20COUNT(%3Fresearcher_of_paper)%20AS%20%3Fpages_per_author)%0A%20%20%20%20WHERE%20%7B%0A%20%20%20%20%20%20%23%20Find%20authors%20associated%20with%20organization%0A%20%20%20%20%20%20FILTER%20EXISTS%20%7B%20%3Fresearcher%20wdt%3AP108%20%7C%20wdt%3AP463%20%7C%20(wdt%3AP1416%20%2F%20wdt%3AP361*)%20wd%3AQ27639076%20.%20%7D%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20%3Fwork%20(wdt%3AP50%7Cwdt%3AP2093)%20%3Fresearcher_of_paper%20.%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20%23%20Disabled%20to%20only%20look%20on%20scholarly%20articles%0A%20%20%20%20%20%20%23%20%3Fwork%20wdt%3AP31%20wd%3AQ13442814%20.%0A%20%20%20%20%20%20%0A%20%20%20%20%20%20%3Fwork%20wdt%3AP50%20%3Fresearcher%20.%0A%20%20%20%20%20%20%3Fwork%20wdt%3AP1104%20%3Fpages%20.%0A%20%20%20%20%20%20%3Fwork%20wdt%3AP577%20%3Fdate%20.%20%0A%20%20%20%20%20%20BIND(STR(YEAR(%3Fdate))%20AS%20%3Fyear)%20%0A%20%20%20%20%20%20%3Fresearcher%20rdfs%3Alabel%20%3Fresearcher_label%20.%20FILTER(LANG(%3Fresearcher_label)%20%3D%20'en')%0A%20%20%20%20%7D%20%0A%20%20%20%20GROUP%20BY%20%3Fwork%20%3Fresearcher_label%20%3Fyear%0A%20%20%7D%0A%7D%0AGROUP%20BY%20%3Fyear%20%3Fresearcher_label%20%0AORDER%20BY%20%3Fyear" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>

## Scholia: una herramienta efectiva para la consulta de los datos

Scholia es un servicio que permite visualizar los datos académicos y científicos de los que dispone Wikidata. Se pueden consultar perfiles de investigadores, temas, especies e incluso sustancia químicas. También de organizaciones, como puede ser el IATEXT.

Si se consulta el perfil del [IATEXT en Scholia](https://scholia.toolforge.org/organization/Q27639076) se pueden observar diferentes aspectos: sus miembros, un gráfico de coautoría (incrustado después de este párrafo), temas en los que publican sus investigadores, publicaciones recientes, producción en número de páginas (incrustado al final del subapartado anterior) y las citas de sus obras, entre otros aspectos.

<iframe style="width: 80vw; height: 50vh; border: none;" src="https://query.wikidata.org/embed.html#%23defaultView%3AGraph%0ASELECT%0A%20%20%3Fauthor1%20%3Fauthor1Label%20%3Fimage1%20%3Frgb%0A%20%20%3Fauthor2%20%3Fauthor2Label%20%3Fimage2%20%0AWITH%20%7B%0A%20%20SELECT%0A%20%20%20%20%3Fauthor1%20(SAMPLE(%3Fimage1_)%20AS%20%3Fimage1)%0A%20%20%20%20%3Fauthor2%20(SAMPLE(%3Fimage2_)%20AS%20%3Fimage2)%0A%20%20%20%20(SAMPLE(%3Frgb_)%20AS%20%3Frgb)%0A%20%20WHERE%20%7B%0A%20%20%20%20wd%3AQ27639076%20%5Ewdt%3AP361*%20%2F%20%5E(%20wdt%3AP108%20%7C%20wdt%3AP1416%20%7C%20wdt%3AP463%20)%20%3Fauthor1%20%2C%20%3Fauthor2%20.%20%0A%20%20%20%20%3Fwork%20wdt%3AP50%20%3Fauthor1%20%2C%20%3Fauthor2%20.%0A%0A%20%20%20%20%23%20Only%20display%20co-authorship%20for%20certain%20types%20of%20documents%0A%20%20%20%20%23%20Journal%20and%20conference%20articles%2C%20books%2C%20not%20(yet%3F)%20software%0A%20%20%20%20VALUES%20%3Fpublication_type%20%7B%20wd%3AQ13442814%20wd%3AQ571%20wd%3AQ26973022%20wd%3AQ17928402%20wd%3AQ947859%20wd%3AQ54670950%20%7D%0A%20%20%20%20FILTER%20EXISTS%20%7B%20%3Fwork%20wdt%3AP31%20%3Fpublication_type%20.%20%7D%0A%0A%20%20%20%20%23%20No%20self-links.%0A%20%20%20%20FILTER%20(%3Fauthor1%20!%3D%20%3Fauthor2)%0A%0A%20%20%20%20%23%20Images%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor1%20wdt%3AP18%20%3Fimage1_%20%7D%0A%20%20%20%20OPTIONAL%20%7B%20%3Fauthor2%20wdt%3AP18%20%3Fimage2_%20%7D%0A%0A%20%20%20%20%23%20Coloring%20of%20the%20nodes%0A%20%20%20%20BIND(%22FFFFFF%22%20AS%20%3Frgb_)%0A%20%20%7D%0A%20%20GROUP%20BY%20%3Fauthor1%20%3Fauthor2%0A%7D%20AS%20%25result%0AWHERE%20%7B%0A%20%20INCLUDE%20%25result%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%2Cda%2Cde%2Ces%2Cfr%2Cjp%2Csv%2Cru%2Czh%22.%0A%20%20%7D%0A%7D%0A" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups"></iframe>

Los dos gráficos incrustados en esta entrada son un ejemplo de cómo se pueden utilizar los datos introducidos en Wikidata con consultas predefinidas por Scholia. No solo se pueden incrustar en el HTML de un sitio web mediante `iframes`, sino que se pueden integrar en prácticamente cualquier lenguaje de programación, como Python, JavaScript o PHP, lo que permite su integración en sistemas de gestión de contenido.

Este servicio, creado por Daniel Mietchen, Egon Willighagen y Finn Årup Nielsen, tiene un gran potencial no solo por lo que nos ofrece, sino por la gran variedad de aspectos que puede abordar. Además, es software libre y abierto, por lo que cualquier persona puede [contribuir a su desarrollas, hacer sugerencias o reportar problemas](https://github.com/fnielsen/scholia).

<hr>

La ciencia abierta es una oportunidad para las instituciones científicas y una necesidad para la sociedad. Wikidata nos proporciona el medio para transferir a la sociedad lo que las instituciones científicas producen. Y Scholia nos facilita consultar estos datos fácilmente.

En Coruja Digital tenemos experiencia con este tipo de proyectos y ofrecemos un servicio concreto dedicado a la transferencia de conocimiento y a la ciencia abierta con Wikidata como base de conocimientos.

Si quieres más información puedes consultar nuestro producto [**Ciencia abierta en Wikidata**](https://corujadigital.tech/ciencia-abierta-wikidata), disponible en nuestro [catálogo de servicios](https://corujadigital.tech/servicios).

Si tienes dudas o quieres más información, puedes [contactar con nosotros](https://corujadigital.tech/contactar). ¡Será un placer responderte! 
