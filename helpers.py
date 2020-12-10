import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

def load_profile():
	return json.loads(read_file(profilePath))

def get_settings():
	profile = load_profile()
	return profile['settings']

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	FILE.write(DATA)
	FILE.close()

def run_command(CMD):
	import subprocess
	print('\n============== Running Command: {}\n'.format(CMD))
	subprocess.call(CMD, shell=True)

def run_command_list(LIST):
	import subprocess
	str = ''
	for item in LIST:
		str += (' ' + item)
	print('\n============== Running Command: {}\n'.format(str))
	subprocess.call(LIST)