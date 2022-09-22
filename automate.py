import sys
import pudb
from pathlib import Path

mainpyfile = sys.argv[1]
args = []

# runscript("t2.py")


pre_run = False
run_as_module = False
dbg = pudb._get_debugger(steal_output=False)

# Note on saving/restoring sys.argv: it's a good idea when sys.argv was
# modified by the script being debugged. It's a bad idea when it was
# changed by the user from the command line. The best approach would be to
# have a "restart" command which would allow explicit specification of
# command line arguments.

if args is not None:
    prev_sys_argv = sys.argv[:]
    if run_as_module:
        sys.argv = args
    else:
        sys.argv = [mainpyfile] + args

# replace pudb's dir with script's dir in front of module search path.
prev_sys_path = sys.path[:]
sys.path[0] = str(Path(mainpyfile).resolve().parent)


# Script may have changed directory. Restore cwd before restart.
import os
cwd = os.getcwd()
os.chdir(cwd)

def get_input_override():
    import time
    time.sleep(0.3)
    return 's'

dbg.ui.screen.get_input = get_input_override
dbg._runscript(mainpyfile)
