from optparse import make_option
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from telemeta.models import *
from telemeta.util.unaccent import unaccent
from teleforma.models import *
from teleforma.views import *
import logging
import codecs


class Command(BaseCommand):
    help = "pull teleforma courses from a remote host"
    admin_email = 'webmaster@parisson.com'
    args = "organization_name department_name"

    def handle(self, *args, **options):
    	organization_name = args[-2]
    	department_name = args[-1]
        view = CourseListView()
        view.pull(organization_name, department_name)
