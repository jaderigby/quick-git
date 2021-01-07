import messages as msg
import sys, helpers, sizzle
import commitAll
import Feature
import Remove
import Branch
import Diff
import Restore
import RestoreBack
import DoStatus
import Back
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

args = sys.argv[2:]

if action == None:
	msg.statusMessage()

elif action == '-action':
	sizzle.do_action(args)

elif action == '-profile':
	sizzle.profile()

elif action == '-helpers':
	sizzle.helpers()

elif action == "all":
    commitAll.execute()

elif action == "feature":
    Feature.execute()

elif action == "remove":
    Remove.execute()

elif action == "branch":
    Branch.execute(args)

elif action == "diff":
    Diff.execute()

elif action == "re":
    Restore.execute(args)

elif action == "reback":
    RestoreBack.execute()

elif action == "status":
    DoStatus.execute()

elif action == "back":
	Back.execute()
# new actions start here
