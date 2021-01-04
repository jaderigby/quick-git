import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
    helpers.run_command('git status')
    selection = helpers.user_selection('Select: ', ['run "qit all"', 'stage all', 'unstage all'])
    if selection is 1:
        helpers.run_command('git add -A')
        helpers.run_command('git status', False)
        commitMessage = raw_input("Commit Message: ")
        helpers.run_command_list(['git', 'commit', '-m', commitMessage])
        helpers.run_command('git push')
    elif selection is 2:
        helpers.run_command('git add -A')
    elif selection is 3:
        helpers.run_command('git reset *')
    msg.done()
