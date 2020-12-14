# quick-git #

## Setup ##

Inside your `Documents` folder, if you don't already have one, create a directory called `bash-tools`.  Then, clone the quick-git repo into this directory.  Inside the `bash-tools` directory, if you don't already have one, create a `.bashrc` file.  Open the `.bashrc` file, and add the following:

```
alias qit="python ~/Documents/bash-tools/quick-git/actions.py"
```

Finally, run the following command:

```
cd ~/Documents/bash-tools/quick-git && mkdir profiles && cd profiles && echo '{\n\t"settings" : {\n\n\t}\n}' >> profile.py
```

## Usage ##

- `qit` = get a list of commands
-  `qit all` = adds all files, commits, and pushes.
- `qit branch` = gives you a list of selectable branches.  enter the number of the branch you wish to switch to and hit "enter"
- `qit feature` = creates a new Square feature branch (local/remote); sets up tracking; switches to branch
- `qit remove` = removes/deletes both local and remote branches; if you are currently on the branch, it first switches you to master, then continues.
- `qit diff` = pulls up a list of modified files for selection.  Once a file is selected, the file will be opened in the difftool specified inside your `profile.py` file.  If you do not have a `profile.py` file, run the following command:

```
cd ~/Documents/bash-tools/quick-git && mkdir profiles
touch profile.py && echo profile.py >> '{\n\t"settings" : {\n\t\t"differ" : ""\n\t}\n}'
```