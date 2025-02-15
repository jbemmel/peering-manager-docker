## Remove first comment(#) on each line to implement this working logging
## example. Add LOGLEVEL environment variable to Peering Manager if you use
## this example & want a different log level.

from os import environ
## Set LOGLEVEL in peering-manager.env or docker-compose.overide.yml to override a logging level of INFO.
LOGLEVEL = 'DEBUG' # environ.get('LOGLEVEL', 'DEBUG')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': LOGLEVEL,
            # 'filters': ['require_debug_false'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        'logging.root': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'napalm.sros': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'peering.manager.peeringdb': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'peering.manager.napalm': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django_auth_ldap': {
            'handlers': ['console',],
            'level': LOGLEVEL,
        }
    }
}
