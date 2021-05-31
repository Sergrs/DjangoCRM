from django.contrib import admin
from django.core.handlers.wsgi import LimitedStream

from .models import User, Lead, Agent

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Agent)