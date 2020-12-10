import messages as msg
import subprocess

# settings = helpers.get_settings()

def execute():
    subprocess.call(['git', 'add', '-A'])
    subprocess.call(['git', 'status'])
    commitMessage = raw_input("Commit Message: ")
    subprocess.call(['git', 'commit', '-m', commitMessage])
    subprocess.call(['git', 'push'])
    print("")
    print("Process Completed")
