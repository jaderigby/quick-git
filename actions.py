import messages as msg
import sys, helpers
import commitAll
import dfile
import Feature
import Remove
import Branch
import Diff
import Restore
import RestoreBack
import DoStatus
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

args = sys.argv[2:]

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
    Restore.execute(args)

elif action == "reback":
    RestoreBack.execute()

elif action == "status":
    DoStatus.execute()
# new actions start here
