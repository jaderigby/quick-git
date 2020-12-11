import messages as msg
import helpers

settings = helpers.get_settings()

def execute():
    listing = helpers.run_command_output('git diff --name-only')
    listingList = listing.splitlines()
    selection = helpers.user_selection('Select file to diff: ', listingList)
    if isinstance(selection, int):
        option = listingList[selection - 1]
        optionList = option.split('/')
        optionList.pop(0) 
        optionPath = '/'.join(optionList)
        helpers.run_command('git difftool {} {}'.format(optionPath, settings['differ']))
    elif selection is 'exit':
        print('\nExiting ...\n')
        msg.done()
    else:
        msg.done()