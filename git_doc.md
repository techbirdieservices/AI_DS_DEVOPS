Git Workflow Documentation
✅ 1. Clone a Repository
git clone https://github.com/techbirdieservices/AI_DS_DEVOPS.git


Explanation:

git clone is used to create a copy of an existing Git repository.

The URL provided points to a remote repository on GitHub.

This command creates a local copy of the AI_DS_DEVOPS repo on your system.

It also automatically sets up the remote URL as origin.

✅ 2. Commit Changes
git commit -m " created agent file"


Explanation:

git commit is used to save your changes to the local repository.

-m "created agent file" adds a commit message describing the change.

Before running this, you must run git add <filename> or git add . to stage the changes.
Example:

git add agent.py

✅ 3. Configure Git User Information (Global)
git config --global user.email "example@gmail.com"
git config --global user.name "example"


Explanation:

These commands set the global Git user identity.

--global means this configuration applies to all repositories on your system.

Git uses this information to tag your commits.

✅ 4. Set a Remote URL
git remote add origin https://github.com/techbirdieservices/AI_DS_DEVOPS.git


Explanation:

git remote add adds a remote repository and names it origin.

If you cloned the repo using git clone, this step is usually already done.

Use this only if the remote was not configured or needs to be re-added.

✅ 5. Rename the Branch
git branch -M main


Explanation:

This renames your current branch to main.

-M forces the rename, even if the main branch already exists.

Git used to default to master, but now main is the standard branch name.

✅ 6. Push Code to Remote
git push -u origin main


Explanation:

git push uploads your local commits to the remote repository.

origin refers to the remote repository.

main is the branch you are pushing to.

-u sets the upstream branch, so you can later use git push and git pull without specifying the branch name again.

🧠 Summary Table
Command	Purpose
git clone <repo>	Clone an existing repo to local machine
git add . or git add <file>	Stage files for commit
git commit -m "message"	Commit changes with message
git config --global	Set global user email and name
git remote add origin <url>	Set up remote URL for pushing code
git branch -M main	Rename current branch to main
git push -u origin main	Push code to remote and set upstream
📝 Tips

Always run git status to see the current status of your working directory.

Use git log to see commit history.

Use .gitignore to prevent unnecessary files (e.g., .pyc, .env) from being committed.

If you'd like, I can export this as a Word or PDF document — just let me know the format you prefer.

