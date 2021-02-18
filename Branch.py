import messages as msg
import subprocess, helpers, os, re

# settings = helpers.get_settings()

def execute(ARGS):
    argDict = helpers.arguments(ARGS)

    out = subprocess.check_output(["git", "branch"]).decode('utf-8')
    outList = out.split()
    if '*' in outList: outList.remove('*')
    if argDict:
        if 'go' in argDict:
            if argDict['go'] == 'back':
                try:
                    helpers.run_command('git checkout -')
                except:
                    print("\nNothing to go back to. Exiting ...")
            elif argDict['go'] == 'master':
                helpers.run_command('git checkout master')
            elif argDict['go'] == 'latest':
                activity = helpers.run_command_output('git for-each-ref --sort=-committerdate refs/heads/', False)
                activityRefined = re.sub('[\w]* commit\t', '', activity)
                latestBranch = activityRefined.split('\n')[0].replace('refs/heads/', '')
                helpers.run_command('git checkout {}'.format(latestBranch))
            elif re.search('[0-9]*', argDict['go']):
                branchName = outList[int(argDict['go']) - 1]
                helpers.run_command('git checkout {}'.format(branchName))
            else:
                print("\nNot a valid selection")
        if 'new' in argDict:
            if argDict['new']:
                nameSelect = argDict['new']
                helpers.run_command('git checkout master')
                helpers.run_command('git pull')
                helpers.run_command('git checkout -b {}'.format(nameSelect))
                helpers.run_command('git push -u origin {}'.format(nameSelect))
    else:
        currentBranch = helpers.run_command_output('git branch --show-current', False).replace('\n','')
        print("")
        selection = helpers.user_selection_with_highlight("Please select branch to checkout: ", outList, False, currentBranch, True)
        if isinstance(selection, int):
            branchName = outList[int(selection) - 1]
            if branchName != currentBranch[0]:
                helpers.run_command('git checkout {}'.format(branchName))
            else:
                msg.exit()
        else:
            msg.exit()

    msg.done()