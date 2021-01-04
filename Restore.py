import messages as msg
import helpers

settings = helpers.get_settings()

def execute(ARGS):
    argDict = helpers.arguments(ARGS)
    if argDict:
        if 'path' in argDict:
            filepath = argDict['path']
            helpers.run_command('git restore --source origin/master -- {FILE}'.format(FILE= filepath))
        elif 'file' in argDict:
            filepath = argDict['file']
            helpers.run_command('git restore --source origin/master -- {FILE}'.format(FILE= filepath))
        elif 'profile' in argDict:
            if argDict['profile'] == 'true':
                for item in settings['restore']:
                    helpers.run_command('git restore --source origin/master -- {FILE}'.format(FILE= item))
            elif argDict['profile'] == 'open':
                helpers.run_command('code {}/profiles/profile.py'.format(helpers.path('util')))
        else:
            filepath = helpers.user_input('File name/path to restore from master: ')
            helpers.run_command('git restore --source origin/master -- {FILE}'.format(FILE= filepath))
    else:
        filepath = helpers.user_input('File name/path to restore from master: ')
        helpers.run_command('git restore --source origin/master -- {FILE}'.format(FILE= filepath))