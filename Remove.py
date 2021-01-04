import messages as msg
import subprocess, helpers, re

# settings = helpers.get_settings()

def execute():
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    out = subprocess.check_output(["git", "branch"])
    outList = out.split()
    if '*' in outList: outList.remove('*')
    if 'master' in outList: outList.remove('master')
    currentBranch = subprocess.check_output(["git", "branch", "--show-current"]).split()
    print("")
    i = 0
    for item in outList:
        i += 1
        if item == currentBranch[0]:
            print(helpers.decorate('green', '[{number}]  {branch}'.format(number=i, branch=item)))
        else:
            print('[{number}]  {branch}'.format(number=i, branch=item))
    selection = input("\nPlease select branch to remove/delete: ")
    branchName = outList[selection - 1]
    print(helpers.decorate('yellow', '\nRemoving: {}\n'.format(branchName)))
    print(branchName)
    print(currentBranch[0])
    if branchName == currentBranch[0]:
        helpers.run_command('git checkout master')
    helpers.run_command('git branch -D {}'.format(branchName))
    helpers.run_command('git push origin --delete {}'.format(branchName))
