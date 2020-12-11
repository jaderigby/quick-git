def example():
	print "process working!"

def statusMessage():
	print '''
[ qit all ]			add, commit, and push all changes
[ qit dfile ]			diff a specific file against HEAD	
[ qit branch ]			get a list of branches; select branch to switch to
[ qit feature ]			creates a new feature branch
[ qit remove ]			removes/deletes both local and remote branch
[ qit diff ]			gives you a selectable list of changed files; opens selected file in your difftool specified inside the profile.py file
'''
def done():
	print('''
[ Process Completed ]
''')