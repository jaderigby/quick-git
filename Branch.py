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
            elif re.search('[0-9]*', argDict['go']):
                branchName = outList[int(argDict['go']) - 1]
                helpers.run_command('git checkout {}'.format(branchName))
            else:
                print("\nNot a valid selection")
    else:
        currentBranch = subprocess.check_output(["git", "branch", "--show-current"]).decode('utf-8').split()
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
        if selection == 'x':
            return
        else:
            branchName = outList[int(selection) - 1]
            if branchName != currentBranch[0]:
                helpers.run_command('git checkout {}'.format(branchName))
            else:
                return
    msg.done()