import messages as msg
import subprocess, helpers

# settings = helpers.get_settings()

def execute():
    nameSelect = helpers.user_input("Please select a name for your feature branch: ")
    currentBranch = helpers.run_command_output('git branch --show-current', False).replace('\n','')
    helpers.run_command('git checkout -b {} {}'.format(nameSelect, currentBranch))
    helpers.run_command('git push -u origin {}'.format(nameSelect))