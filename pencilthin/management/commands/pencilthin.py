from django.core.management.base import BaseCommand, CommandError
from django.template import Context, Template
from django.conf import settings
import subprocess

class Command(BaseCommand):
    def handle(self, *args, **options):
        t = Template(subprocess.check_output("handlebars -m %s" % " ".join(settings.BAR_FILES), shell = True))
        output = t.render(Context({}))
        f = open(settings.BAR_OUT, 'w')
        f.write(output)
        f.close()
