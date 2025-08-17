# Development Container Configuration

This directory contains the configuration for GitHub Codespaces and VS Code Dev Containers.

## What's Included

- **Python 3.11** environment
- **Git** and **GitHub CLI** tools
- **Node.js LTS** for any frontend tooling
- **Port forwarding** for the development server (port 8000)
- **VS Code extensions** for Python development, web development, and code formatting

## Automatic Setup

When you open this repository in GitHub Codespaces or VS Code with the Dev Containers extension:

1. The environment will automatically install Python dependencies from `requirements.txt`
2. Python linting and formatting tools will be configured
3. The development server port (8000) will be forwarded
4. All necessary VS Code extensions will be installed

## Usage

After the container is created, you can start the development server by running:

```bash
python server.py
```

The server will be available at the forwarded port, accessible through your browser.

## Customization

You can modify `devcontainer.json` to:
- Add more VS Code extensions
- Change Python version
- Add additional development tools
- Configure different port forwarding
- Set custom environment variables
