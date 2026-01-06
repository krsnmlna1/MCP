from mcp.server.fastmcp import FastMCP
import argparse

# Import tools
from tools.component_generator import generate_component, REACT_COMPONENT_TEMPLATE
from tools.project_setup import setup_project, list_templates
from tools.package_manager import install_dependencies, add_package, remove_package, detect_package_manager
from tools.github_integration import clone_repository, push_changes, create_branch

# Initialize the MCP server
mcp = FastMCP("Web-Frontend")


# Component Generation Tools
@mcp.tool()
def web_generate_component(
    component_name: str,
    framework: str = "react",
    props: str = None,
    description: str = None
) -> str:
    """
    Generate a component boilerplate for React, Vue, or HTML.
    
    Args:
        component_name: Component name in PascalCase (e.g., 'MyComponent')
        framework: 'react' (default), 'vue', or 'html'
        props: JSON string of props, e.g. '[{"name": "title", "type": "string"}]'
        description: Optional description of the component
    """
    return generate_component(component_name, framework, props, description)


# Project Setup Tools
@mcp.tool()
def web_setup_project(
    project_name: str,
    template: str = "vite-react-ts",
    path: str = None
) -> str:
    """
    Setup a new frontend project with a specified template.
    
    Args:
        project_name: Name of the project
        template: Project template ('react', 'vite-react-ts', 'nextjs', 'vite-vue-ts', etc.)
        path: Base directory path for the project (optional)
    """
    return setup_project(project_name, template, path)


@mcp.tool()
def web_list_project_templates() -> str:
    """List all available project templates."""
    return list_templates()


# Package Manager Tools
@mcp.tool()
def web_detect_package_manager(cwd: str = None) -> str:
    """Detect which package manager is used in the project (npm, yarn, pnpm)."""
    pm = detect_package_manager()
    import json
    return json.dumps({
        "status": "success",
        "package_manager": pm
    })


@mcp.tool()
def web_install_dependencies(cwd: str = None) -> str:
    """
    Install dependencies for the current project.
    
    Args:
        cwd: Working directory (optional)
    """
    return install_dependencies(cwd)


@mcp.tool()
def web_add_package(
    package_name: str,
    dev: bool = False,
    save_exact: bool = False,
    cwd: str = None
) -> str:
    """
    Add a package to the project.
    
    Args:
        package_name: Package name, optionally with version (e.g., 'react', 'react@18.2.0')
        dev: Install as dev dependency (default: false)
        save_exact: Save exact version without ^ or ~ prefix (default: false)
        cwd: Working directory (optional)
    """
    return add_package(package_name, dev, save_exact, cwd)


@mcp.tool()
def web_remove_package(
    package_name: str,
    cwd: str = None
) -> str:
    """
    Remove a package from the project.
    
    Args:
        package_name: Name of the package to remove
        cwd: Working directory (optional)
    """
    return remove_package(package_name, cwd)


# GitHub Integration Tools
@mcp.tool()
def web_github_clone(
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
    return clone_repository(repo_url, directory, branch)


@mcp.tool()
def web_github_push(
    message: str,
    branch: str = None,
    cwd: str = None
) -> str:
    """
    Commit and push changes to GitHub.
    
    Args:
        message: Commit message
        branch: Target branch (optional, uses current branch by default)
        cwd: Working directory (optional)
    """
    return push_changes(message, branch, cwd)


@mcp.tool()
def web_github_create_branch(
    branch_name: str,
    from_branch: str = None,
    cwd: str = None
) -> str:
    """
    Create and checkout a new Git branch.
    
    Args:
        branch_name: Name of the new branch
        from_branch: Base branch to create from (optional)
        cwd: Working directory (optional)
    """
    return create_branch(branch_name, from_branch, cwd)


def main():
    parser = argparse.ArgumentParser(description="Web Frontend MCP Server")
    parser.add_argument("--transport", default="stdio", choices=["stdio", "sse"], help="Transport mode")
    args = parser.parse_args()

    mcp.run(transport=args.transport)


if __name__ == "__main__":
    main()
