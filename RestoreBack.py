import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
    branch = helpers.run_command_output('git branch --show-current', False)
    branch = branch.replace('\n', '')
    branchOrigin = 'origin/{}'.format(branch)
    filepath = helpers.user_input('File name/path to restore from last commit: ')
    # helpers.run_command('git restore --source {BRANCH} -- {FILE}'.format(BRANCH= branch, FILE= filepath))
    helpers.run_command_list(['git', 'restore', '--source', branchOrigin, '--', filepath])