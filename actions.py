import sys, status, helpers
import commitAll
import dfile
import testModule
import Feature
import Remove
import Branch
import Diff
import Restore
import RestoreBack
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

if action == 'status' or action == None:
	status.execute()

elif action == "all":
    commitAll.execute()

elif action == "dfile":
    dfile.execute()

elif action == "test":
    testModule.execute()

elif action == "feature":
    Feature.execute()

elif action == "remove":
    Remove.execute()

elif action == "branch":
    Branch.execute()

elif action == "diff":
    Diff.execute()

elif action == "re":
    Restore.execute()

elif action == "reback":
    RestoreBack.execute()
# new actions start here
