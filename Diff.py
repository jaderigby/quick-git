import messages as msg
import helpers

settings = helpers.get_settings()

def execute():
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
    msg.done()