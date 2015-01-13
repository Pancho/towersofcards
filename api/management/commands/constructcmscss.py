import os
import logging


from django.core.management.base import NoArgsCommand
from django.template import Context, Template


from api import ASSETS
from api import mongo
from towersofcards import version


logger = logging.getLogger(__name__)


CSS_TEMPLATE = '''/* This is a generated file - it's highly recommended that you don't change it manually, but rather */
/* use the scripts provided to do that (running "python manage.py constructcmscss" should do the trick) */
{% for asset in assets %}
.toc-{{ asset.slug }} {background:transparent url(/media/img/cms/{{ asset_group_name }}/{{ asset.slug }}.png?v={{ static_file_version }}) left top no-repeat;}{% endfor %}
'''


class Command(NoArgsCommand):
	def handle_noargs(self, **options):
		root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../media/')

		for asset_group_name in ASSETS.keys():
			print(asset_group_name)
			if asset_group_name == 'gamemaps':
				continue

			css_file_path = '%scss/%s.css' % (root, asset_group_name)
			if os.path.isfile(css_file_path):
				os.remove(css_file_path)

			css_file = open(css_file_path, 'w')

			template = Template(CSS_TEMPLATE)
			ctx = Context({
				'asset_group_name': asset_group_name,
				'assets': mongo.db[asset_group_name].find(),
				'static_file_version': version.STATIC_FILES_VERSION,
			})

			css_file.write(template.render(ctx))
			css_file.close()
