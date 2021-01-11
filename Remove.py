import messages as msg
import subprocess, helpers, re

# settings = helpers.get_settings()

def execute(ARGS):
    argDict = helpers.arguments(ARGS)

    outList = helpers.run_command_output('git branch').split()
    if '*' in outList: outList.remove('*')
    if 'master' in outList: outList.remove('master')
    currentBranch = helpers.run_command_output('git branch --show-current').replace('\n', '')
    
    selection = helpers.user_selection("\nPlease select branch to remove/delete: ", outList, currentBranch)
    if selection != 'exit':
        branchName = outList[selection - 1]
        print(helpers.decorate('yellow', '\nRemoving: {}'.format(branchName)))
        if argDict:
            if 'local' in argDict or 'l' in argDict:
                if argDict['local'] == 'true' or argDict['local'] == 't' or argDict['l'] == 'true' or argDict['l'] == 't':
                    if branchName == currentBranch:
                        helpers.run_command('git checkout master')
                    helpers.run_command('git branch -D {}'.format(branchName))
            elif 'remote' in argDict or 'r' in argDict:
                if argDict['remote'] == 'true' or argDict['remote'] == 't' or argDict['remote'] == 'true' or argDict['remote'] == 't':
                    helpers.run_command('git push origin --delete {}'.format(branchName))

        else:
            if branchName == currentBranch:
                helpers.run_command('git checkout master')
            helpers.run_command('git branch -D {}'.format(branchName))
            helpers.run_command('git push origin --delete {}'.format(branchName))
    else:
        print("\nExiting ...\n")

    msg.done()
