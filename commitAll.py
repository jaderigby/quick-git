import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
    helpers.run_command('git add -A')
    helpers.run_command('git status')
    commitMessage = raw_input("Commit Message: ")
    helpers.run_command_list(['git', 'commit', '-m', commitMessage])
    helpers.run_command('git push')
    msg.done()
