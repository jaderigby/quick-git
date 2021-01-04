import messages as msg
import subprocess, helpers

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
    currentBranch = subprocess.check_output(["git", "branch", "--show-current"]).split()
    print("")
    i = 0
    for item in outList:
        i += 1
        if item == currentBranch[0]:
            print(helpers.decorate('green', ' *   {branch}'.format(number=i, branch=item)))
        else:
            print('[{number}]  {branch}'.format(number=i, branch=item))
    print('\n[x]  Exit\n')
    selection = helpers.user_input("Please select branch to checkout: ")
    if selection is 'x':
        return
    else:
        branchName = outList[int(selection) - 1]
        if branchName != currentBranch[0]:
            helpers.run_command('git checkout {}'.format(branchName))
        else:
            return