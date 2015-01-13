import re
import os
import time


from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
	def handle_noargs(self, *args, **options):
		# Create a timestamp
		time_now = int(time.time())

		# Update settings for JS deploy
		towersofcards_js_version = r'staticFilesVersion: [0-9]+'
		towersofcards_js_version_replace = 'staticFilesVersion: %s' % time_now

		towersofcards_js_contents = open('media/js/towersofcards.js', 'r').read()

		re_towersofcards_js_version = re.compile(towersofcards_js_version, re.MULTILINE)
		towersofcards_js_content = re_towersofcards_js_version.sub(towersofcards_js_version_replace, towersofcards_js_contents)

		towersofcards_js_file = open('media/js/towersofcards.js', 'w')
		towersofcards_js_file.write(towersofcards_js_content)
		towersofcards_js_file.close()

		# Update settings for deploy
		settings_version = r'STATIC_FILES_VERSION = [0-9]+'
		settings_version_replace = 'STATIC_FILES_VERSION = %s' % time_now

		settings_contents = open('towersofcards/version.py', 'r').read()

		re_settings_version = re.compile(settings_version, re.MULTILINE)
		settings_content = re_settings_version.sub(settings_version_replace, settings_contents)

		settings_file = open('towersofcards/version.py', 'w')
		settings_file.write(settings_content)
		settings_file.close()

		# Update css files
		css_replace = r'url\(([^\)]*)\)'
		css_replace_with = r'url(\1?v=%s)' % time_now
		existing_version = r'\?v=[0-9]+'

		css_files = os.listdir('media/css')

		for css_file_name in css_files:
			if css_file_name == 'font-awesome.css':
				continue
			if css_file_name.find('.css') >= 0:
				css_file_name = '%s/%s' % ('media/css', css_file_name)
				contents = open(css_file_name, 'r').read()

				re_css = re.compile(existing_version, re.MULTILINE)
				contents = re_css.sub('', contents)

				re_css = re.compile(css_replace, re.MULTILINE)
				contents = re_css.sub(css_replace_with, contents)

				wr = open(css_file_name, 'w')
				wr.write(contents)
				wr.close()

		# Prepare image list for preloading
		image_files = []

		for path, dirs, files in os.walk("media/img/"):
			for f in files:
				if f.endswith('png') or f.endswith('jpg') or f.endswith('jpeg') or f.endswith('gif'):
					image_files.append('/%s/%s' % (path.replace('\\', '/'), f))
					image_files.append('/%s/%s?v=%s' % (path.replace('\\', '/'), f, time_now))

		image_files_list = r'var TowersOfCardsImageList = \[([^\]]*)\];$'
		image_file_list_replace = 'var TowersOfCardsImageList = %s;' % image_files

		default_js_contents = open('media/js/common.js', 'r').read()
		re_image_files_list = re.compile(image_files_list, re.MULTILINE)
		default_js_content = re_image_files_list.sub(image_file_list_replace, default_js_contents)

		default_js_file = open('media/js/common.js', 'w')
		default_js_file.write(default_js_content)
		default_js_file.close()