import messages as msg
import subprocess, helpers

# settings = helpers.get_settings()

def execute():
    nameSelect = helpers.user_input("Please select a name for your feature branch: ")
    helpers.run_command('git checkout master')
    helpers.run_command('git pull')
    helpers.run_command('git checkout -b {}'.format(nameSelect))
    helpers.run_command('git push -u origin {}'.format(nameSelect))
    # helpers.run_command('git branch -u origin/{}'.format(nameSelect))