import helpers, json

actionList = json.loads(helpers.read_file('{}/{}'.format(helpers.path('util'), 'action-list.json')))

def statusMessage():
	if len(actionList['actions']) > 0:
		print("")
		for item in actionList['actions']:
			print('''[ {} {} ]\t\t{}'''.format(actionList['alias'], item['name'], item['description']))
		print("")
	else:
		print('''
quick-git is working successfully!
''')

def done():
	print('''
[ Process Completed ]
''')

def exit():
	print("\nExiting ...\n")

def example():
	print("process working!")

def set_differ():
	statusMsg = '''
Please add the differ configuration to your profile file.
For example:

{
	"settings" : {
		"differ": "-y -t Kaleidoscope"
	}
}
'''
	print(statusMsg)