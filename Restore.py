import messages as msg
import helpers

settings = helpers.get_settings()

def execute(ARGS):
    argDict = helpers.arguments(ARGS)
    if argDict:
        if 'path' in argDict:
            filepath = argDict['path']
        elif 'file' in argDict:
            filepath = argDict['file']
        elif 'profile' in argDict and argDict['profile'] == 'true':
            for item in settings['restore']:
                helpers.run_command('git restore --source origin/master -- {FILE}'.format(FILE= item))
        else:
            filepath = helpers.user_input('File name/path to restore from master: ')
    else:
        filepath = helpers.user_input('File name/path to restore from master: ')
        helpers.run_command('git restore --source origin/master -- {FILE}'.format(FILE= filepath))