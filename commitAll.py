import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
    helpers.run_command('git add -A')
    helpers.run_command('git status', False)
    commitMessage = helpers.user_input("Commit Message: ")
    helpers.run_command('git commit -m "{}"'.format(commitMessage))
    # helpers.run_command(['git', 'commit', '-m', commitMessage])
    helpers.run_command('git push')
    msg.done()
