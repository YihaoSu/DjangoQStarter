"""
ASGI config for django_q_starter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/

"""
import os
import sys
from pathlib import Path

from django.core.asgi import get_asgi_application

# This allows easy placement of apps within the interior
# niot_docker directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / 'django_q_starter'))

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

# This application object is used by any ASGI server configured to use this file.
django_application = get_asgi_application()
