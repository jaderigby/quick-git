import helpers, json

actionList = json.loads(helpers.read_file('action-list.json'))

def statusMessage():
	if len(actionList['actions']) > 0:
		for item in actionList['actions']:
			print('''\n[ {} {} ]\t\t{}
'''.format(actionList['alias'], item['name'], item['description']))
	else:
		print('''
quick-git is working successfully!
''')

def done():
	print('''
[ Process Completed ]
''')

def example():
	print "process working!"