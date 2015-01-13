from django.core.management import call_command
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		call_command('importdata')
		call_command('constructcmscss')
		call_command('preparedeploy')
