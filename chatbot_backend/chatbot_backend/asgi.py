"""
ASGI config for chatbot_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_backend.settings')
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from chatbot_api import app as chatbot_app
app = FastAPI()
django_app = get_asgi_application()
fastapi_app = FastAPI()
fastapi_app.mount('/chatbot', django_app)

app.mount('/django', WSGIMiddleware(django_app))
app.mount('/chatbot', chatbot_app)

application = app
