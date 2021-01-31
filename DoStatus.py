import messages as msg
import helpers

settings = helpers.get_settings()

def execute():
    while True:
        fileList = helpers.run_command_output('git diff --name-only', False).splitlines()
        untrackedListing = helpers.run_command_output('git ls-files --others --exclude-standard', False).splitlines()
        combinedList = fileList + untrackedListing
        helpers.run_command('git status')
        if len(combinedList) == 0:
            break
        selection = helpers.status_selection('Selection: ', ['diff', 'push all', 'unstage all', 'push/exclude'])
        if selection == 1:
            if settings:
                if 'differ' in settings:
                    while True:
                        selection = helpers.user_selection('Select file to diff: ', fileList)
                        if isinstance(selection, int):
                            option = fileList[selection - 1]
                            currentPath = helpers.run_command_output('pwd', False)
                            helpers.run_command('git difftool {}/{} {}'.format(currentPath.replace('\n', ''), option, settings['differ']))
                        elif selection == 'exit':
                            print('\nExiting ...\n')
                            break
                else:
                    msg.set_differ()
        elif selection == 2:
            helpers.run_command('git add -A')
            helpers.run_command('git status', False)
            commitMessage = helpers.user_input("Commit Message: ")
            helpers.run_command('git commit -m "{}"'.format(commitMessage))
            helpers.run_command('git push')
            break
        elif selection == 3:
            helpers.run_command('git reset *')
        elif selection == 4:
            print("\n=====================")
            fileSelection = helpers.user_selection('push all, except: [eg: 1,3,4] ', combinedList, True)
            helpers.run_command('git add -A')
            if fileSelection != 'exit':
                for item in fileSelection:
                    helpers.run_command('git reset {}'.format(combinedList[item - 1]))
            helpers.run_command('git status')
            commitMessage = helpers.user_input("Commit Message: ")
            helpers.run_command('git commit -m "{}"'.format(commitMessage))
            helpers.run_command('git push')
            break
        elif selection == 'exit':
            break
    msg.done()
