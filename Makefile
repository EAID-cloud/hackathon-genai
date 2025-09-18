# Resolve uv binary path (fallback to ~/.local/bin/uv if not in PATH)
UV := $(shell command -v uv 2>/dev/null || echo $(HOME)/.local/bin/uv)

# Install dependencies using uv package manager
install:
	@command -v $(UV) >/dev/null 2>&1 || { echo "uv is not installed. Installing uv..."; curl -LsSf https://astral.sh/uv/0.6.12/install.sh | sh; }
	$(UV) sync --dev
# Launch local dev playground
playground:
	@echo "==============================================================================="
	@echo "| 🚀 Starting your agent playground...                                        |"
	@echo "|                                                                             |"
	@echo "| 💡 Try asking: What's the weather in San Francisco?                         |"
	@echo "|                                                                             |"
	@echo "| 🔍 IMPORTANT: Select the 'app' folder to interact with your agent.          |"
	@echo "==============================================================================="
	$(UV) run adk web . --port 8501 --reload_agents

# Deploy the agent remotely
backend:
	# Export dependencies to requirements file using uv export.
	$(UV) export --no-hashes --no-header --no-dev --no-emit-project --no-annotate > .requirements.txt 2>/dev/null || \
	$(UV) export --no-hashes --no-header --no-dev --no-emit-project > .requirements.txt && $(UV) run app/agent_engine_app.py

# Set up development environment resources using Terraform
setup-dev-env:
	PROJECT_ID=$$(gcloud config get-value project) && \
	(cd deployment/terraform/dev && terraform init && terraform apply --var-file vars/env.tfvars --var dev_project_id=$$PROJECT_ID --auto-approve)

# Run unit and integration tests
test:
	$(UV) run pytest tests/unit && $(UV) run pytest tests/integration

# Run code quality checks (codespell, ruff, mypy)
lint:
	$(UV) sync --dev --extra lint
	$(UV) run codespell
	$(UV) run ruff check . --diff
	$(UV) run ruff format . --check --diff
	$(UV) run mypy .