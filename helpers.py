import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

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

def path(TYPE):
	import os
	if TYPE == 'user':
		return os.path.expanduser('~/')
	elif TYPE == 'util' or TYPE == 'utility':
		return os.path.dirname(os.path.realpath(__file__))
	else:
		return False

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	with open(FILEPATH, 'w') as f: f.write(DATA)

def run_command(CMD, option = True):
	import subprocess
	shellStatus = True
	str = ''
	showCmd = CMD
	if isinstance(CMD, list):
		shellStatus = False
		for item in CMD:
			str += (' ' + item)
		showCmd = str
	if option:
		print('\n============== Running Command: {}\n'.format(showCmd))
	subprocess.call(CMD, shell=shellStatus)

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
			result = out.decode('utf-8')

	return result

def decorate(COLOR, STRING):
	bcolors = {
		 'lilac' : '\033[95m'
		,'blue' : '\033[94m'
		,'cyan' : '\033[96m'
		,'green' : '\033[92m'
		,'yellow' : '\033[93m'
		,'red' : '\033[91m'
		,'bold' : '\033[1m'
		,'underline' : '\033[4m'
		,'endc' : '\033[0m'
	}

	return bcolors[COLOR] + STRING + bcolors['endc']

def user_input(STRING):
	try:
		return raw_input(STRING)
	except:
		return input(STRING)

def list_expander(LIST):
    baseList = LIST.replace(' ', '').split(',')
    expandedList = []
    for item in baseList:
        if '-' in item:
            rangeList = item.split('-')
            tempList = [elem for elem in range(int(rangeList[0]), int(rangeList[1]) + 1)]
            expandedList += tempList
        else:
            expandedList.append(int(item))
    return expandedList

# generates a user selection session, where the passed in list is presented as numbered selections; selecting "x" or just hitting enter results in the string "exit" being returned. Any invaild selection is captured and presented with the message "Please select a valid entry"
def user_selection(DESCRIPTION, LIST, LIST_SELECT = False, CURRENT = ''):
	import re
	str = ''
	for i, item in enumerate(LIST, start=1):
		if item == CURRENT:
			str += decorate('green', '\n[{index}] {item}'.format(index=i, item=item))
		else:
			str += '\n[{index}] {item}'.format(index=i, item=item)
	str += '\n\n[x] Exit\n'

	finalAnswer = False

	while True:
		print(str)
		selection = user_input('{}'.format(DESCRIPTION))
		if LIST_SELECT:
			pat = re.compile("[0-9,\- ]+")
		else:
			pat = re.compile("[0-9]+")
		if pat.match(selection):
			if LIST_SELECT:
				selection = list_expander(selection)
			else:
				selection = int(selection)
		if isinstance(selection, int) or isinstance(selection, list):
			finalAnswer = selection
			break
		elif selection == 'x':
			finalAnswer = 'exit'
			break
		elif selection == '':
			finalAnswer = 'exit'
			break
		else:
			print("\nPlease select a valid entry...")
	return finalAnswer

def arguments(ARGS, DIVIDER=':'):
	return dict(item.split('{}'.format(DIVIDER)) for item in ARGS)


# custom helpers start here
# =========================

def separation():
	return '     '

def status_selection(DESCRIPTION, LIST):
	import re
	str = ''
	print('')
	for i, item in enumerate(LIST, start=1):
		str += '[{index}] {item}{separator}'.format(index=i, item=item, separator=separation())
	str += '[x] Exit\n'

	finalAnswer = False

	while True:
		print(str)
		selection = user_input('{}'.format(DESCRIPTION))
		pat = re.compile("[0-9]+")
		if pat.match(selection):
			selection = int(selection)
		if isinstance(selection, int):
			finalAnswer = selection
			break
		elif selection == 'x':
			finalAnswer = 'exit'
			break
		elif selection == '':
			finalAnswer = 'exit'
			break
		else:
			print("\nPlease select a valid entry...")
	return finalAnswer

def remove_local_branch(CURRENT_BRANCH, BRANCH_TO_REMOVE):
	if BRANCH_TO_REMOVE == CURRENT_BRANCH:
		run_command('git checkout master')
	run_command('git branch -D {}'.format(BRANCH_TO_REMOVE))

def remove_remote_branch(BRANCH_TO_REMOVE):
	run_command('git push origin --delete {}'.format(BRANCH_TO_REMOVE))

def check_context(OBJ):
	if OBJ:
		if 'local' in OBJ:
			if OBJ['local'] == 'true' or OBJ['local'] == 't':
				return 'removeLocalOnly'
		elif 'l' in OBJ:
			if OBJ['l'] == 'true' or OBJ['l'] == 't':
				return 'removeLocalOnly'
		elif 'remote' in OBJ:
			if OBJ['remote'] == 'true' or OBJ['remote'] == 't':
				return 'removeRemoteOnly'
		elif 'r' in OBJ:
			if OBJ['r'] == 'true' or OBJ['r'] == 't':
				return 'removeRemoteOnly'
	else:
		return 'removeLocalAndRemote'