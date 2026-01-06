import json
import subprocess
import os
from pathlib import Path


PROJECT_TEMPLATES = {
    "react": {
        "command": "npx",
        "args": ["create-react-app"],
        "description": "Create React App"
    },
    "react-ts": {
        "command": "npx",
        "args": ["create-react-app", "--template", "typescript"],
        "description": "Create React App with TypeScript"
    },
    "vite-react": {
        "command": "npm",
        "args": ["create", "vite@latest", "--", "--template", "react"],
        "description": "Vite + React"
    },
    "vite-react-ts": {
        "command": "npm",
        "args": ["create", "vite@latest", "--", "--template", "react-ts"],
        "description": "Vite + React + TypeScript"
    },
    "vite-vue": {
        "command": "npm",
        "args": ["create", "vite@latest", "--", "--template", "vue"],
        "description": "Vite + Vue"
    },
    "vite-vue-ts": {
        "command": "npm",
        "args": ["create", "vite@latest", "--", "--template", "vue-ts"],
        "description": "Vite + Vue + TypeScript"
    },
    "nextjs": {
        "command": "npx",
        "args": ["create-next-app@latest"],
        "description": "Next.js"
    }
}


def setup_project(
    project_name: str,
    template: str = "vite-react-ts",
    path: str = None
) -> str:
    """
    Setup a new frontend project with specified template.
    
    Args:
        project_name: Name of the project
        template: Template to use (react, vite-react-ts, nextjs, etc.)
        path: Base path where project will be created (default: current directory)
    """
    try:
        # Validate project name
        if not project_name or not project_name.replace("-", "").replace("_", "").isalnum():
            return json.dumps({
                "status": "error",
                "message": "Invalid project name. Use alphanumeric characters, hyphens, or underscores"
            })
        
        # Check if template exists
        if template not in PROJECT_TEMPLATES:
            available = ", ".join(PROJECT_TEMPLATES.keys())
            return json.dumps({
                "status": "error",
                "message": f"Unknown template '{template}'. Available: {available}"
            })
        
        # Determine project path
        base_path = path or os.getcwd()
        project_path = os.path.join(base_path, project_name)
        
        # Check if directory already exists
        if os.path.exists(project_path):
            return json.dumps({
                "status": "error",
                "message": f"Directory '{project_path}' already exists"
            })
        
        template_info = PROJECT_TEMPLATES[template]
        
        # Build command
        cmd = [template_info["command"]] + template_info["args"] + [project_name]
        
        return json.dumps({
            "status": "ready",
            "project_name": project_name,
            "template": template,
            "template_description": template_info["description"],
            "path": project_path,
            "command": " ".join(cmd),
            "note": "Run the command above to create the project. Install dependencies with 'cd {} && npm install' or equivalent".format(project_name)
        })
    
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })


def list_templates() -> str:
    """List all available project templates."""
    templates = []
    for key, value in PROJECT_TEMPLATES.items():
        templates.append({
            "name": key,
            "description": value["description"]
        })
    
    return json.dumps({
        "status": "success",
        "templates": templates
    })
