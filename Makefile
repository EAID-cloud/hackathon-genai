<<<<<<< HEAD
# Resolve uv binary path (fallback to ~/.local/bin/uv if not in PATH)
UV := $(shell command -v uv 2>/dev/null || echo $(HOME)/.local/bin/uv)

# Install dependencies using uv package manager
install:
	@command -v $(UV) >/dev/null 2>&1 || { echo "uv is not installed. Installing uv..."; curl -LsSf https://astral.sh/uv/0.6.12/install.sh | sh; }
	$(UV) sync --dev
=======
# Install dependencies using uv package manager
install:
	@command -v uv >/dev/null 2>&1 || { echo "uv is not installed. Installing uv..."; curl -LsSf https://astral.sh/uv/0.6.12/install.sh | sh; source $HOME/.local/bin/env; }
	uv sync --dev
>>>>>>> e35e7c2 (Initial commit)
# Launch local dev playground
playground:
	@echo "==============================================================================="
	@echo "| 🚀 Starting your agent playground...                                        |"
	@echo "|                                                                             |"
	@echo "| 💡 Try asking: What's the weather in San Francisco?                         |"
	@echo "|                                                                             |"
	@echo "| 🔍 IMPORTANT: Select the 'app' folder to interact with your agent.          |"
	@echo "==============================================================================="
<<<<<<< HEAD
	$(UV) run adk web . --port 8501 --reload_agents
=======
	uv run adk web . --port 8501 --reload_agents
>>>>>>> e35e7c2 (Initial commit)

# Deploy the agent remotely
backend:
	# Export dependencies to requirements file using uv export.
<<<<<<< HEAD
	$(UV) export --no-hashes --no-header --no-dev --no-emit-project --no-annotate > .requirements.txt 2>/dev/null || \
	$(UV) export --no-hashes --no-header --no-dev --no-emit-project > .requirements.txt && $(UV) run app/agent_engine_app.py
=======
	uv export --no-hashes --no-header --no-dev --no-emit-project --no-annotate > .requirements.txt 2>/dev/null || \
	uv export --no-hashes --no-header --no-dev --no-emit-project > .requirements.txt && uv run app/agent_engine_app.py
>>>>>>> e35e7c2 (Initial commit)

# Set up development environment resources using Terraform
setup-dev-env:
	PROJECT_ID=$$(gcloud config get-value project) && \
	(cd deployment/terraform/dev && terraform init && terraform apply --var-file vars/env.tfvars --var dev_project_id=$$PROJECT_ID --auto-approve)

# Run unit and integration tests
test:
<<<<<<< HEAD
	$(UV) run pytest tests/unit && $(UV) run pytest tests/integration

# Run code quality checks (codespell, ruff, mypy)
lint:
	$(UV) sync --dev --extra lint
	$(UV) run codespell
	$(UV) run ruff check . --diff
	$(UV) run ruff format . --check --diff
	$(UV) run mypy .
=======
	uv run pytest tests/unit && uv run pytest tests/integration

# Run code quality checks (codespell, ruff, mypy)
lint:
	uv sync --dev --extra lint
	uv run codespell
	uv run ruff check . --diff
	uv run ruff format . --check --diff
	uv run mypy .
>>>>>>> e35e7c2 (Initial commit)
