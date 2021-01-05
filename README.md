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
- `qit all` = adds all files, commits, and pushes.
- `qit branch` = lets you switch branches by selecting from a list.
- `qit feature` = creates a new feature branch (local/remote), sets up tracking, and then switches to the branch
- `qit remove` = removes/deletes both local and remote branches; if you are currently on the branch, it first switches you to master, then continues.
- `qit diff` = gives you a selectable list of changed files;opens selected file in your difftool as specified inside the profile.py file. If you do not have a profile file, run the following:

```
qit -profile
```

Then, the profile file configuration should look something like the following:

```

```