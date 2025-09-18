# my-agent

A base ReAct agent built with Google's Agent Development Kit (ADK)
<<<<<<< HEAD
Agent generated with [`googleCloudPlatform/agent-starter-pack`](https://github.com/GoogleCloudPlatform/agent-starter-pack) version `0.15.0`
=======
Agent generated with [`googleCloudPlatform/agent-starter-pack`](https://github.com/GoogleCloudPlatform/agent-starter-pack) version `0.14.1`
>>>>>>> e35e7c2 (Initial commit)

## Project Structure

This project is organized as follows:

```
<<<<<<< HEAD
my-awesome-agent/
=======
my-agent/
>>>>>>> e35e7c2 (Initial commit)
├── app/                 # Core application code
│   ├── agent.py         # Main agent logic
│   ├── agent_engine_app.py # Agent Engine application logic
│   └── utils/           # Utility functions and helpers
├── .cloudbuild/         # CI/CD pipeline configurations for Google Cloud Build
├── deployment/          # Infrastructure and deployment scripts
├── notebooks/           # Jupyter notebooks for prototyping and evaluation
├── tests/               # Unit, integration, and load tests
├── Makefile             # Makefile for common commands
├── GEMINI.md            # AI-assisted development guide
└── pyproject.toml       # Project dependencies and configuration
```

## Requirements

Before you begin, ensure you have:
- **uv**: Python package manager (used for all dependency management in this project) - [Install](https://docs.astral.sh/uv/getting-started/installation/) ([add packages](https://docs.astral.sh/uv/concepts/dependencies/) with `uv add <package>`)
- **Google Cloud SDK**: For GCP services - [Install](https://cloud.google.com/sdk/docs/install)
- **Terraform**: For infrastructure deployment - [Install](https://developer.hashicorp.com/terraform/downloads)
- **make**: Build automation tool - [Install](https://www.gnu.org/software/make/) (pre-installed on most Unix-based systems)

<<<<<<< HEAD
## Local Development & Testing

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd my-agent
```

### 2. Install Dependencies

```bash
make install
```

### 3. Configure Google Cloud (Required for LLM calls)

#### Option A: Use Application Default Credentials (Recommended)

```bash
# Authenticate with Google Cloud
gcloud auth login
gcloud auth application-default login

# Set your project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable aiplatform.googleapis.com logging.googleapis.com storage.googleapis.com cloudtrace.googleapis.com --project YOUR_PROJECT_ID
```

#### Option B: Use API Key (Alternative)

```bash
export GOOGLE_API_KEY="your-api-key"
export GOOGLE_GENAI_USE_VERTEXAI=False
export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
```

### 4. Run Local Development Server

```bash
make playground
```

Open http://localhost:8501 in your browser to test the agent.

### 5. Test the Agent

Try these sample prompts:
- "What's the weather in San Francisco?"
- "What time is it in San Francisco?"
- "Hello, how can you help me?"

## Google Cloud Deployment

### Prerequisites

1. **Google Cloud Project**: Create a project in [Google Cloud Console](https://console.cloud.google.com/)
2. **Billing**: Ensure billing is enabled for your project
3. **APIs**: Enable required APIs (done automatically in setup below)

### 1. One-Time Setup

#### Create Service Account for Deployment

```bash
# Set your project ID
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=us-central1

# Create service account
gcloud iam service-accounts create agent-engine-sa \
  --display-name="Agent Engine SA" \
  --project $GOOGLE_CLOUD_PROJECT

# Grant required roles
gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="serviceAccount:agent-engine-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="serviceAccount:agent-engine-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/serviceusage.serviceUsageConsumer"

gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="serviceAccount:agent-engine-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/logging.logWriter"

gcloud projects add-iam-policy-binding $GOOGLE_CLOUD_PROJECT \
  --member="serviceAccount:agent-engine-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
  --role="roles/cloudtrace.agent"

# Enable APIs
gcloud services enable aiplatform.googleapis.com logging.googleapis.com storage.googleapis.com cloudtrace.googleapis.com --project $GOOGLE_CLOUD_PROJECT
```

#### Set Environment Variables

```bash
export AGENT_ENGINE_SERVICE_ACCOUNT="agent-engine-sa@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com"
```

### 2. Deploy to Vertex AI Agent Engine

```bash
# Deploy using Makefile (uses environment variables)
make backend

# Or deploy directly with explicit parameters
uv run app/agent_engine_app.py \
  --agent-name my-awesome-agent \
  --project $GOOGLE_CLOUD_PROJECT \
  --location $GOOGLE_CLOUD_LOCATION \
  --service-account $AGENT_ENGINE_SERVICE_ACCOUNT
```

### 3. Verify Deployment

After successful deployment, check `deployment_metadata.json` for the Agent Engine ID:

```bash
cat deployment_metadata.json
```

View your deployed agent in the [Google Cloud Console](https://console.cloud.google.com/vertex-ai/agent-engines).

=======

## Quick Start (Local Testing)

Install required packages and launch the local development environment:

```bash
make install && make playground
```

>>>>>>> e35e7c2 (Initial commit)
## Commands

| Command              | Description                                                                                 |
| -------------------- | ------------------------------------------------------------------------------------------- |
| `make install`       | Install all required dependencies using uv                                                  |
| `make playground`    | Launch Streamlit interface for testing agent locally and remotely |
| `make backend`       | Deploy agent to Agent Engine |
| `make test`          | Run unit and integration tests                                                              |
| `make lint`          | Run code quality checks (codespell, ruff, mypy)                                             |
| `make setup-dev-env` | Set up development environment resources using Terraform                         |
| `uv run jupyter lab` | Launch Jupyter notebook                                                                     |

For full command options and usage, refer to the [Makefile](Makefile).

<<<<<<< HEAD
## GitHub Publishing & Security

### 1. Environment Configuration

Create a `.env.example` file for documentation:

```bash
# Copy this to .env and fill in your values
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
AGENT_ENGINE_SERVICE_ACCOUNT=agent-engine-sa@your-project-id.iam.gserviceaccount.com

# Optional: Use API key instead of ADC
# GOOGLE_API_KEY=your-api-key
# GOOGLE_GENAI_USE_VERTEXAI=False
```

### 2. CI/CD Pipeline

The project includes Cloud Build configuration in `.cloudbuild/`. To set up automated deployment:

1. Connect your repository to Google Cloud Build
2. Configure build triggers
3. Set up the required secrets in Cloud Build

See [deployment/README.md](deployment/README.md) for detailed CI/CD setup instructions.
=======
>>>>>>> e35e7c2 (Initial commit)

## Usage

This template follows a "bring your own agent" approach - you focus on your business logic, and the template handles everything else (UI, infrastructure, deployment, monitoring).

1. **Prototype:** Build your Generative AI Agent using the intro notebooks in `notebooks/` for guidance. Use Vertex AI Evaluation to assess performance.
2. **Integrate:** Import your agent into the app by editing `app/agent.py`.
3. **Test:** Explore your agent functionality using the Streamlit playground with `make playground`. The playground offers features like chat history, user feedback, and various input types, and automatically reloads your agent on code changes.
<<<<<<< HEAD
4. **Deploy:** Use the deployment instructions above to deploy to Google Cloud.
=======
4. **Deploy:** Set up and initiate the CI/CD pipelines, customizing tests as necessary. Refer to the [deployment section](#deployment) for comprehensive instructions. For streamlined infrastructure deployment, simply run `uvx agent-starter-pack setup-cicd`. Check out the [`agent-starter-pack setup-cicd` CLI command](https://googlecloudplatform.github.io/agent-starter-pack/cli/setup_cicd.html). Currently supports GitHub with both Google Cloud Build and GitHub Actions as CI/CD runners.
>>>>>>> e35e7c2 (Initial commit)
5. **Monitor:** Track performance and gather insights using Cloud Logging, Tracing, and the Looker Studio dashboard to iterate on your application.

The project includes a `GEMINI.md` file that provides context for AI tools like Gemini CLI when asking questions about your template.


<<<<<<< HEAD
## Monitoring and Observability

The application uses OpenTelemetry for comprehensive observability with all events being sent to Google Cloud Trace and Logging for monitoring and to BigQuery for long term storage.

### View Logs and Metrics

1. **Cloud Logging**: View agent logs in [Google Cloud Console](https://console.cloud.google.com/logs)
2. **Cloud Trace**: Monitor request traces in [Cloud Trace](https://console.cloud.google.com/traces)
3. **Looker Studio Dashboard**: Use [this dashboard template](https://lookerstudio.google.com/reporting/46b35167-b38b-4e44-bd37-701ef4307418/page/tEnnC) for visualizing events in BigQuery

### Agent Engine Status

Check your deployed agent status:
```bash
# List all agent engines
gcloud ai agent-engines list --location=us-central1 --project=YOUR_PROJECT_ID

# Get specific agent details
gcloud ai agent-engines describe AGENT_ENGINE_ID --location=us-central1 --project=YOUR_PROJECT_ID
```

## Troubleshooting

### Common Issues

1. **"Default credentials not found"**
   - Run `gcloud auth application-default login`
   - Or set `GOOGLE_APPLICATION_CREDENTIALS` environment variable

2. **"Permission denied" errors**
   - Ensure service account has required roles
   - Check project ID is correct

3. **Agent Engine deployment fails**
   - Verify APIs are enabled
   - Check service account permissions
   - Review Cloud Build logs

4. **Local playground won't start**
   - Ensure `uv` is installed and in PATH
   - Check port 8501 is available
   - Verify Google Cloud authentication

### Getting Help

- Check the [Google Cloud documentation](https://cloud.google.com/docs)
- Review [Vertex AI Agent Engines guide](https://cloud.google.com/vertex-ai/docs/agent-engines)
- Open an issue in this repository for project-specific problems
=======
## Deployment

> **Note:** For a streamlined one-command deployment of the entire CI/CD pipeline and infrastructure using Terraform, you can use the [`agent-starter-pack setup-cicd` CLI command](https://googlecloudplatform.github.io/agent-starter-pack/cli/setup_cicd.html). Currently supports GitHub with both Google Cloud Build and GitHub Actions as CI/CD runners.

### Dev Environment

You can test deployment towards a Dev Environment using the following command:

```bash
gcloud config set project <your-dev-project-id>
make backend
```


The repository includes a Terraform configuration for the setup of the Dev Google Cloud project.
See [deployment/README.md](deployment/README.md) for instructions.

### Production Deployment

The repository includes a Terraform configuration for the setup of a production Google Cloud project. Refer to [deployment/README.md](deployment/README.md) for detailed instructions on how to deploy the infrastructure and application.


## Monitoring and Observability
> You can use [this Looker Studio dashboard](https://lookerstudio.google.com/reporting/46b35167-b38b-4e44-bd37-701ef4307418/page/tEnnC
) template for visualizing events being logged in BigQuery. See the "Setup Instructions" tab to getting started.

The application uses OpenTelemetry for comprehensive observability with all events being sent to Google Cloud Trace and Logging for monitoring and to BigQuery for long term storage.
>>>>>>> e35e7c2 (Initial commit)
