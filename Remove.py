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
    
    # Assign context
    context = helpers.check_context(argDict)

    # select branch/s to remove
    selections = helpers.user_selection_with_highlight("\nPlease select branch to remove/delete: ", localBranchList, True, currentBranch)
    
    if selections != 'exit':
        branchesString = '\n'
        branchesToRemoveList = []
        for branchItem in selections:
            branchName = localBranchList[branchItem - 1]
            branchesString += '- {}\n'.format(localBranchList[branchItem - 1])
            branchesToRemoveList.append(branchName)

        if context == 'removeLocalOnly':
            if len(selections) > 1:
                print('\n\nRemoving local branches: \n{}'.format(helpers.decorate('yellow', branchesString)))
            else:
                print('\n\nRemoving local branch: {}'.format(helpers.decorate('yellow', branchName)))
            confirm = helpers.user_input("\nAre you sure? [y/n] ")
            if confirm == 'y':
                for branch in branchesToRemoveList:
                    helpers.remove_local_branch(currentBranch, branch)
        elif context == 'removeRemoteOnly':
            if len(selections) > 1:
                print('\n\nRemoving remote branches: {}'.format(helpers.decorate('yellow', branchesString)))
            else:
                print('\n\nRemoving remote branch: {}'.format(helpers.decorate('yellow', branchName)))
            confirm = helpers.user_input("\nAre you sure? [y/n] ")
            if confirm == 'y':
                for branch in branchesToRemoveList:
                    helpers.remove_remote_branch(branch)
        elif context == 'removeLocalAndRemote':
            print('\n\nRemoving branch: {}'.format(helpers.decorate('yellow', branchName)))
            confirm = helpers.user_input("\nAre you sure? [y/n] ")
            if confirm == 'y':
                for branch in branchesToRemoveList:
                    helpers.remove_local_branch(currentBranch, branch)
                    helpers.remove_remote_branch(branch)
    else:
        print("\nExiting ...\n")

    msg.done()
