import messages as msg
import sys, helpers
import commitAll
import dfile
import testModule
import Feature
import Remove
import Branch
import Diff
import Restore
import RestoreBack
import Status
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

if action == None:
	msg.statusMessage()

elif action == "all":
    commitAll.execute()

elif action == "dfile":
    dfile.execute()

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

elif action == "status":
    Status.execute()
# new actions start here
