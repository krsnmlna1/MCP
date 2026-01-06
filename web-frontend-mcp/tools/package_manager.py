import json
import subprocess
import os


def detect_package_manager() -> str:
    """Detect which package manager is being used in the current project."""
    if os.path.exists("package-lock.json"):
        return "npm"
    elif os.path.exists("yarn.lock"):
        return "yarn"
    elif os.path.exists("pnpm-lock.yaml"):
        return "pnpm"
    else:
        return "npm"  # default


def install_dependencies(cwd: str = None) -> str:
    """
    Install dependencies for the current project.
    
    Args:
        cwd: Working directory (default: current directory)
    """
    try:
        work_dir = cwd or os.getcwd()
        
        if not os.path.exists(os.path.join(work_dir, "package.json")):
            return json.dumps({
                "status": "error",
                "message": f"No package.json found in {work_dir}"
            })
        
        pm = detect_package_manager()
        cmd = [pm, "install"]
        
        return json.dumps({
            "status": "ready",
            "command": " ".join(cmd),
            "package_manager": pm,
            "cwd": work_dir,
            "note": "Run the command above to install dependencies"
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })


def add_package(
    package_name: str,
    dev: bool = False,
    save_exact: bool = False,
    cwd: str = None
) -> str:
    """
    Add a package to the project.
    
    Args:
        package_name: Name of the package (can include version: 'package@1.0.0')
        dev: Install as dev dependency
        save_exact: Save exact version (^, ~, or no prefix)
        cwd: Working directory
    """
    try:
        work_dir = cwd or os.getcwd()
        
        if not os.path.exists(os.path.join(work_dir, "package.json")):
            return json.dumps({
                "status": "error",
                "message": f"No package.json found in {work_dir}"
            })
        
        pm = detect_package_manager()
        
        # Build command based on package manager
        if pm == "npm":
            cmd = ["npm", "install"]
            if dev:
                cmd.append("--save-dev")
            if save_exact:
                cmd.append("--save-exact")
            cmd.append(package_name)
        elif pm == "yarn":
            cmd = ["yarn", "add"]
            if dev:
                cmd.append("--dev")
            if save_exact:
                cmd.append("--exact")
            cmd.append(package_name)
        elif pm == "pnpm":
            cmd = ["pnpm", "add"]
            if dev:
                cmd.append("--save-dev")
            if save_exact:
                cmd.append("--exact")
            cmd.append(package_name)
        
        return json.dumps({
            "status": "ready",
            "command": " ".join(cmd),
            "package_manager": pm,
            "package_name": package_name,
            "dev": dev,
            "cwd": work_dir,
            "note": "Run the command above to add the package"
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })


def remove_package(
    package_name: str,
    cwd: str = None
) -> str:
    """
    Remove a package from the project.
    
    Args:
        package_name: Name of the package
        cwd: Working directory
    """
    try:
        work_dir = cwd or os.getcwd()
        
        if not os.path.exists(os.path.join(work_dir, "package.json")):
            return json.dumps({
                "status": "error",
                "message": f"No package.json found in {work_dir}"
            })
        
        pm = detect_package_manager()
        
        if pm == "npm":
            cmd = ["npm", "uninstall", package_name]
        elif pm == "yarn":
            cmd = ["yarn", "remove", package_name]
        elif pm == "pnpm":
            cmd = ["pnpm", "remove", package_name]
        
        return json.dumps({
            "status": "ready",
            "command": " ".join(cmd),
            "package_manager": pm,
            "package_name": package_name,
            "cwd": work_dir,
            "note": "Run the command above to remove the package"
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })
