import messages as msg
import helpers

settings = helpers.get_settings()

def execute():
    listing = helpers.run_command_output('git diff --name-only')
    listingList = listing.splitlines()
    selection = helpers.user_selection('Select file to diff: ', listingList)
    if isinstance(selection, int):
        option = listingList[selection - 1]
        print("option: " + option)
        currentPath = helpers.run_command_output('pwd')
        print('git difftool {}/{} {}'.format(currentPath, option, settings['differ']))
        helpers.run_command('git difftool {}/{} {}'.format(currentPath, option, settings['differ']))
    elif selection is 'exit':
        print('\nExiting ...\n')
        msg.done()
    else:
        msg.done()