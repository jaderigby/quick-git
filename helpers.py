import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

# path for current user. Example: "cd ~/"
def root():
	import os
	return os.path.expanduser('~/')

# path to utility
def self_path():
	import os
	return os.path.dirname(os.path.realpath(__file__))

def load_profile():
	import os
	if os.path.exists(profilePath):
		return json.loads(read_file(profilePath))
	else:
		return json.loads("{}")

def get_settings():
	profile = load_profile()
	if 'settings' in profile:
		return profile['settings']
	else:
		return False

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	FILE.write(DATA)
	FILE.close()

def user_input(STRING):
    return raw_input(STRING)

def run_command(CMD, option = True):
	import subprocess
	if option:
		print('\n============== Running Command: {}\n'.format(CMD))
	subprocess.call(CMD, shell=True)

def run_command_output(CMD, option = True):
	import subprocess
	if option:
		print('\n============== Outputting Command: {}\n'.format(CMD))
	result = False
	if CMD != None:
		process = subprocess.Popen(CMD, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
		out, err = process.communicate()

		if err:
			print(err)
		
		else:
			result = out

	return result

def run_command_list(LIST):
	import subprocess
	str = ''
	for item in LIST:
		str += (' ' + item)
	print('\n============== Running Command: {}\n'.format(str))
	subprocess.call(LIST)

# returns PascalCased/camelCased strings as strings with spaces. Acronyms, such as NASASatellite will resolve to "NASA Satellite"
# Be advised: does not account for numbers
def titled(NAME):
	import re
	charList = []
	pat = re.compile('[A-Z]')
	nameList = list(NAME)
	for i, char in enumerate(nameList):
		if (i + 1 < len(nameList) and i - 1 >= 0):
			up_ahead = nameList[i + 1]
			from_behind = nameList[i - 1]
		else:
			up_ahead = ''
			from_behind = ''
		if pat.match(char) and i != 0:
			if pat.match(from_behind) and pat.match(up_ahead):
				charList.append(char)
			else:
				charList.append(' ')
				charList.append(char)
		else:
			charList.append(char)
	return ''.join(charList)

def kabob(NAME):
	str = titled(NAME)
	return str.replace(' ', '-').lower()

def user_selection(DESCRIPTION, LIST):
	import re
	str = ''
	for i, item in enumerate(LIST, start=1):
		str += '\n[{index}] {item}'.format(index=i, item=item)
	str += '\n\n[x] Exit\n'

	finalAnswer = False

	while True:
		print(str)
		selection = raw_input('{}'.format(DESCRIPTION))
		pat = re.compile("[0-9]+")
		if pat.match(selection):
			selection = int(selection)
		if isinstance(selection, int):
			finalAnswer = selection
			break
		elif selection is 'x':
			finalAnswer = 'exit'
			break
		elif selection is '':
			finalAnswer = 'exit'
			break
		else:
			print("\nPlease select a valid entry...")
	return finalAnswer