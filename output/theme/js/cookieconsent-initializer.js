message = "Este sitio web utiliza unas pocas cookies para garantizar una mejor experiencia de usuario."
allow = "Permitir cookies"
link = "Más información en nuestra política de privacidad."
deny = "Rechazar"
href = "aviso-legal"

window.cookieconsent.initialise({
	overrideHTML: true,
	"palette": {
		"popup": {
			"background": "#252e39"
		},
			"button": {
							"background": "#14a7d0"
			}
	},
	"theme": "edgeless",
	"type": "opt-out",
	"content": {
		"message": message,
		"allow": allow,
		"deny": deny,
		"link": link,
		"href": href
	}
});
