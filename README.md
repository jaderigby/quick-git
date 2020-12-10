# quick-git #

## Install ##

Inside your `Documents` folder, if you don't already have one, create a directory called `bash-tools`.  Then, clone the quick-git repo into this directory.  Inside the `bash-tools` directory, if you don't already have one, create a `.bashrc` file.  Add the following to it:

```
alias qit="python ~/Documents/bash-tools/quick-git/actions.py"
```

## Usage ##

- `qit` = get a list of commands
-  `qit all` = adds all files, commits, and pushes.
- `qit branch` = gives you a list of selectable branches.  enter the number of the branch you wish to switch to and hit "enter"
- `qit feature` = creates a new Square feature branch (local/remote); sets up tracking; switches to branch
- `qit remove` = removes/deletes both local and remote branches; if you are currently on the branch, it first switches you to master, then continues.