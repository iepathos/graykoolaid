response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('HOME'),URL('default','index')==URL(),URL('default','index'),[]),
(T('ABOUT'),URL('default','about')==URL(),URL('default','about'),[]),
(T('PROJECTS'),URL('default','projects')==URL(),URL('default','projects'),[]),
(T('CONTACT'),URL('default','contact')==URL(),URL('default','contact'),[]),
]