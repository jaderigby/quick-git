import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
    branch = helpers.run_command_output('git branch --show-current', False)
    filepath = helpers.user_input('File name/path to restore from master: ')
    helpers.run_command('git checkout master && git pull && git checkout {CURRENT_BRANCH}'.format(CURRENT_BRANCH= branch))
    helpers.run_command('git restore --source master -- {FILE}'.format(FILE= filepath))