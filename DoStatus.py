import messages as msg
import helpers

settings = helpers.get_settings()

def execute():
    helpers.run_command('git status')
    selection = helpers.status_selection('Selection: ', ['diff', 'unstage all', 'push/exclude'])
    if selection == 1:
        while True:
            listing = helpers.run_command_output('git diff --name-only')
            listingList = listing.splitlines()
            selection = helpers.user_selection('Select file to diff: ', listingList)
            if isinstance(selection, int):
                option = listingList[selection - 1]
                currentPath = helpers.run_command_output('pwd', False)
                helpers.run_command('git difftool {}/{} {}'.format(currentPath.replace('\n', ''), option, settings['differ']))
            elif selection == 'exit':
                print('\nExiting ...\n')
                break
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
