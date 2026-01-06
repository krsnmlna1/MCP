import json
import subprocess
import os


def clone_repository(
    repo_url: str,
    directory: str = None,
    branch: str = None
) -> str:
    """
    Clone a GitHub repository.
    
    Args:
        repo_url: Full GitHub URL (https://github.com/user/repo.git)
        directory: Directory to clone into (optional)
        branch: Specific branch to clone (optional)
    """
    try:
        # Validate URL
        if not repo_url.startswith("https://github.com/") and not repo_url.startswith("git@github.com:"):
            return json.dumps({
                "status": "error",
                "message": "Invalid GitHub URL format"
            })
        
        cmd = ["git", "clone"]
        
        if branch:
            cmd.extend(["--branch", branch])
        
        cmd.append(repo_url)
        
        if directory:
            cmd.append(directory)
        
        return json.dumps({
            "status": "ready",
            "command": " ".join(cmd),
            "repo_url": repo_url,
            "branch": branch or "default",
            "directory": directory or "auto-detected from repo name",
            "note": "Run the command above to clone the repository"
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })


def push_changes(
    message: str,
    branch: str = None,
    cwd: str = None
) -> str:
    """
    Commit and push changes to GitHub.
    
    Args:
        message: Commit message
        branch: Branch to push to (default: current branch)
        cwd: Working directory
    """
    try:
        work_dir = cwd or os.getcwd()
        
        if not os.path.exists(os.path.join(work_dir, ".git")):
            return json.dumps({
                "status": "error",
                "message": f"Not a git repository: {work_dir}"
            })
        
        # Check if there are changes to commit
        status_cmd = ["git", "-C", work_dir, "status", "--porcelain"]
        
        commands = [
            f"git -C {work_dir} add .",
            f'git -C {work_dir} commit -m "{message}"'
        ]
        
        if branch:
            commands.append(f"git -C {work_dir} push origin {branch}")
        else:
            commands.append(f"git -C {work_dir} push")
        
        return json.dumps({
            "status": "ready",
            "commands": commands,
            "message": message,
            "branch": branch or "current",
            "cwd": work_dir,
            "note": "Run the commands above to commit and push changes"
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })


def create_branch(
    branch_name: str,
    from_branch: str = None,
    cwd: str = None
) -> str:
    """
    Create and checkout a new branch.
    
    Args:
        branch_name: Name of the new branch
        from_branch: Base branch to create from (default: main/master)
        cwd: Working directory
    """
    try:
        work_dir = cwd or os.getcwd()
        
        if not os.path.exists(os.path.join(work_dir, ".git")):
            return json.dumps({
                "status": "error",
                "message": f"Not a git repository: {work_dir}"
            })
        
        # Validate branch name
        if not branch_name or " " in branch_name:
            return json.dumps({
                "status": "error",
                "message": "Invalid branch name (no spaces allowed)"
            })
        
        commands = []
        
        if from_branch:
            commands.append(f"git -C {work_dir} checkout -b {branch_name} {from_branch}")
        else:
            commands.append(f"git -C {work_dir} checkout -b {branch_name}")
        
        return json.dumps({
            "status": "ready",
            "commands": commands,
            "branch_name": branch_name,
            "from_branch": from_branch or "current",
            "cwd": work_dir,
            "note": "Run the command above to create and checkout the branch"
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })
