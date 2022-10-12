from django.contrib import admin

from oc_lettings_site.lettings.models import Letting
from oc_lettings_site.lettings.models import Address

admin.site.register(Letting)
admin.site.register(Address)
