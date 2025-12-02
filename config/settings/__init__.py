DJANGO_SETTINGS_MODULE = 'config.settings.dev'



if DJANGO_SETTINGS_MODULE == 'config.settings.dev':
    from .dev import *
    
if DJANGO_SETTINGS_MODULE == 'config.settings.dev':
    from .pro import *
    
else:
    from .dev import *