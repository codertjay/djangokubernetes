"""
WSGI config for djangok8 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path
import dotenv
from django.core.wsgi import get_wsgi_application

CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASE_DIR / ".env"

print('fike path ---------------------',ENV_FILE_PATH)
dotenv.read_dotenv(str(ENV_FILE_PATH))

dotenv.read_dotenv(str(ENV_FILE_PATH))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangok8.settings')

application = get_wsgi_application()
