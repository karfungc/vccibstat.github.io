import subprocess

def git_push(commit_message):
    try:
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True)
        print("Added changes to staging.")

        # Commit changes
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"Committed changes: {commit_message}")

        # Push changes
        subprocess.run(['git', 'push'], check=True)
        print("Pushed changes to remote repository.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    commit_message = "Updated"
    git_push(commit_message)
