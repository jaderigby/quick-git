import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
    helpers.run_command('git status')
    selection = helpers.status_selection('Selection: ', ['"qit all"', 'unstage all', 'push/exclude'])
    if selection == 1:
        helpers.run_command('git add -A')
        helpers.run_command('git status', False)
        commitMessage = raw_input("Commit Message: ")
        helpers.run_command_list(['git', 'commit', '-m', commitMessage])
        helpers.run_command('git push')
    elif selection == 2:
        helpers.run_command('git reset *')
    elif selection == 3:
        print("\n=====================")
        fileList = helpers.run_command_output('git diff --name-only', False).splitlines()
        fileSelection = helpers.user_list_selection('push all, except: [eg: 1,3,4] ', fileList)
        helpers.run_command('git add -A')
        if isinstance(fileSelection, list):
            for item in fileSelection:
                helpers.run_command('git reset {}'.format(item))
        elif fileSelection != 'exit':
            helpers.run_command('git reset {}'.format(fileSelection))
        helpers.run_command('git status')
        commitMessage = helpers.user_input("Commit Message: ")
        helpers.run_command('git commit -m "{}"'.format(commitMessage))
        helpers.run_command('git push')
    msg.done()
