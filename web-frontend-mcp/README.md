# 🎨 Web Frontend MCP Server

An AI-powered MCP server for frontend development. Generate components, scaffold projects, manage packages, and integrate with GitHub—all through natural language!

## Features

✅ **Component Generation** - Generate React, Vue, or HTML components instantly  
✅ **Project Scaffolding** - Setup modern frontend projects (Vite, Next.js, etc.)  
✅ **Package Management** - Install, add, remove packages with auto-detection  
✅ **GitHub Integration** - Clone repos, push changes, manage branches  

## Supported Frameworks

- **React** (JavaScript & TypeScript)
- **Vue** (JavaScript & TypeScript)
- **Next.js**
- **Vite** + React/Vue
- **HTML** (vanilla)

## Available Tools

### Component Generation
- `web_generate_component` - Generate boilerplate components with props
- `web_list_project_templates` - See all available project templates

### Project Setup
- `web_setup_project` - Initialize a new frontend project
- `web_list_project_templates` - View available templates

### Package Management
- `web_detect_package_manager` - Detect npm/yarn/pnpm
- `web_install_dependencies` - Install all dependencies
- `web_add_package` - Add a new package
- `web_remove_package` - Remove a package

### GitHub Integration
- `web_github_clone` - Clone a repository
- `web_github_push` - Commit and push changes
- `web_github_create_branch` - Create a new branch

## Installation

1. **Clone or download this folder**

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure with GitHub Copilot CLI:**

Add to your MCP configuration (or use `/mcp add` in Copilot CLI):

```json
{
  "mcpServers": {
    "web-frontend": {
      "command": "python",
      "args": ["C:\\path\\to\\web-frontend-mcp\\main.py"]
    }
  }
}
```

Or for Claude Desktop:
```json
{
  "mcpServers": {
    "web-frontend": {
      "command": "python",
      "args": ["/path/to/web-frontend-mcp/main.py"]
    }
  }
}
```

## Usage Examples

### Generate a React Component
```
Create a Button component in React with onClick and label props
```

### Setup a New Project
```
Setup a new Vite + React + TypeScript project called my-app
```

### Add Dependencies
```
Add React Router and TailwindCSS to my project
```

### Clone and Setup
```
Clone https://github.com/user/repo.git and install dependencies
```

### Push to GitHub
```
Commit all changes with message "Add new features" and push to main
```

## Requirements

- Python 3.8+
- Node.js (for npm/yarn/pnpm)
- Git (for GitHub integration)
- GitHub Copilot CLI or Claude Desktop

## Project Structure

```
web-frontend-mcp/
├── main.py                    # MCP server entry point
├── requirements.txt           # Python dependencies
├── tools/
│   ├── component_generator.py # React/Vue/HTML component generation
│   ├── project_setup.py       # Project scaffolding templates
│   ├── package_manager.py     # npm/yarn/pnpm operations
│   └── github_integration.py  # Git & GitHub operations
└── README.md                  # This file
```

## Notes

- All tools return JSON with status, command, and instructions
- **No commands are executed automatically** - you review and run them
- Supports npm, yarn, and pnpm automatically
- Works with both HTTPS and SSH GitHub URLs

## Future Enhancements

- [ ] CSS framework templates (TailwindCSS, Bootstrap)
- [ ] Component library integration
- [ ] Testing setup (Jest, Vitest, etc.)
- [ ] Linting configuration
- [ ] Environment variable setup
- [ ] Deploy to Vercel/Netlify

## License

MIT

Created with ❤️ for frontend developers
