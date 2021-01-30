import messages as msg
import subprocess, helpers, re

# settings = helpers.get_settings()

def execute(ARGS):
    argDict = helpers.arguments(ARGS)

    # get list of local branches; filter out '*' and 'master'
    localBranchList = helpers.run_command_output('git branch', False).split()
    if '*' in localBranchList: localBranchList.remove('*')
    if 'master' in localBranchList: localBranchList.remove('master')

    # get current branch
    currentBranch = helpers.run_command_output('git branch --show-current', False).replace('\n', '')
    
    # select branch/s to remove
    selection = helpers.user_selection("\nPlease select branch to remove/delete: ", localBranchList, False, currentBranch)
    
    if selection != 'exit':
        branchName = localBranchList[selection - 1]
        if argDict:
            if 'local' in argDict:
                if argDict['local'] == 'true' or argDict['local'] == 't':
                    print('\n\nRemoving local branch: {}'.format(helpers.decorate('yellow', branchName)))
                    confirm = helpers.user_input("\nAre you sure? [y/n] ")
                    if confirm == 'y':
                        helpers.remove_local_branch(currentBranch, branchName)
            elif 'l' in argDict:
                if argDict['l'] == 'true' or argDict['l'] == 't':
                    print('\n\nRemoving local branch: {}'.format(helpers.decorate('yellow', branchName)))
                    confirm = helpers.user_input("\nAre you sure? [y/n] ")
                    if confirm == 'y':
                        helpers.remove_local_branch(currentBranch, branchName)
            elif 'remote' in argDict:
                if argDict['remote'] == 'true' or argDict['remote'] == 't':
                    print('\n\nRemoving remote branch: {}'.format(helpers.decorate('yellow', branchName)))
                    confirm = helpers.user_input("\nAre you sure? [y/n] ")
                    if confirm == 'y':
                        helpers.remove_remote_branch(branchName)
            elif 'r' in argDict:
                if argDict['r'] == 'true' or argDict['r'] == 't':
                    print('\n\nRemoving remote branch: {}'.format(helpers.decorate('yellow', branchName)))
                    confirm = helpers.user_input("\nAre you sure? [y/n] ")
                    if confirm == 'y':
                        helpers.remove_remote_branch(branchName)

        else:
            print('\n\nRemoving branch: {}'.format(helpers.decorate('yellow', branchName)))
            confirm = helpers.user_input("\nAre you sure? [y/n] ")
            if confirm == 'y':
                helpers.remove_local_branch(currentBranch, branchName)
                helpers.remove_remote_branch(branchName)
    else:
        print("\nExiting ...\n")

    msg.done()
