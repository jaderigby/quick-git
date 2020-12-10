import messages as msg
import subprocess

# settings = helpers.get_settings()

def execute():
    subprocess.call(['git', 'status'])
