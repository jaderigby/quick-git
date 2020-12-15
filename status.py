import messages as msg
import helpers

# settings = helpers.get_settings()

def execute():
    helpers.run_command('git status')
    msg.done()
