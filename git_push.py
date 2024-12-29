import git

# Path to your local repository
repo_path = "./"

# Initialize a Git repository object
repo = git.Repo(repo_path)

# Add all changes to the staging area
repo.git.add(all=True)

# Commit the changes
repo.index.commit("Commit message")

# Push the changes to the remote repository
origin = repo.remote("origin")
origin.push()