Okay, here's the content formatted entirely in Markdown, suitable for a GitHub README:

Markdown

## 🤖 College Course Recommendation Agent with Google ADK & Vertex RAG

This project leverages Google's Agent Development Kit (ADK) with the Vertex AI RAG Engine to recommend college courses based on a student's interest survey.

---

### ✅ Prerequisites

* A **Google Cloud Platform (GCP)** account.
* **Billing enabled** for your project.
* **Google Cloud CLI** installed: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
* **Python 3.9+** and `virtualenv` or `venv`.

---

### 🛠️ Step 1: Create a Google Cloud Project

First, create your GCP project.

```bash
gcloud projects create collegeagent-458307 --name="College Agent Project"
Then, set it as your active project for all subsequent commands:

Bash

gcloud config set project collegeagent-458307
💳 Step 2: Enable and Link Billing
You need to link a billing account to your project to use Google Cloud services.

Go to Billing: Navigate to the Google Cloud Billing page.
Create a Billing Account: If you don't have one, select "Create billing account" and follow the prompts.
Link Billing Account to Project:

If your project collegeagent-458307 isn't linked, select "Link a billing account" and choose your new or existing billing account.
If it's already linked, go to "Manage billing accounts," select your billing account, and check the project details. You can click the three dots next to your project to change the billing account if needed.
Alternatively, you can link it via the CLI:

Bash

gcloud beta billing projects link collegeagent-458307 --billing-account=YOUR_BILLING_ACCOUNT_ID
To find your billing account ID:

Bash

gcloud beta billing accounts list
📦 Step 3: Enable Required APIs
Enable the necessary Google Cloud APIs for AI Platform, Discovery Engine, Storage, and Cloud Build:

Bash

gcloud services enable aiplatform.googleapis.com \
                         discoveryengine.googleapis.com \
                         storage.googleapis.com \
                         cloudbuild.googleapis.com
🧠 Step 4: Create RAG Corpus in Vertex AI RAG Engine
This step involves setting up the knowledge base for your chatbot.

Enable Vertex AI API: Ensure the aiplatform.googleapis.com API is enabled (which you did in Step 3).
Navigate to Vertex AI RAG Engine: In the Google Cloud Console, search for "Vertex AI" and then find "RAG Engine" in the left navigation.
Create Corpus:
Choose the default region us-central1.
Click "Create Corpus."
Give your corpus a clear name and an optional description.
Upload Documents:
Upload your course documents (e.g., syllabi, course descriptions) in supported formats like .txt or .pdf. You can upload multiple documents.
Configure Corpus Settings:
Press "Continue."
Choose text-embedding-004 as the embedding model.
Select RAG managed vector store.
Press "Create Corpus."
Copy Resource Name: Once the corpus is created, go to its "Details" page. Copy the full "Resource name." It will look something like: projects/YOUR_PROJECT_NUMBER/locations/us-central1/ragCorpora/YOUR_CORPUS_ID.
🔑 Step 5: Set Up Environment Variables
Create a file named .env in your project's root directory and add the following lines. Make sure to replace the placeholder values with your actual project ID and the RAG Corpus resource name you copied.

Code snippet

# Use Vertex AI as the backend
GOOGLE_GENAI_USE_VERTEXAI=1

# Vertex backend config
GOOGLE_CLOUD_PROJECT=collegeagent-458307
GOOGLE_CLOUD_LOCATION=us-central1

# Your created corpus path (paste the copied Resource name here)
RAG_CORPUS=projects/YOUR_PROJECT_NUMBER/locations/us-central1/ragCorpora/YOUR_CORPUS_ID
🧪 Step 6: Run Your Agent
Finally, install dependencies and run your agent locally to test it.

Install dependencies:

Bash

pip install -r requirements.txt
Activate environment variables:

Bash

source .env
Authenticate GCP CLI: Navigate to the parent directory adk_chatbot (or wherever your main.py is located) and run:

Bash

gcloud auth application-default login
Set Quota Project:

Bash

gcloud auth application-default set-quota-project collegeagent-458307
Test the API locally:

Bash

python main.py
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# College Agent - Sullamussalam Science College Assistant

A Flask-based REST API service that provides an AI assistant for Sullamussalam Science College using Google's Vertex AI and RAG (Retrieval Augmented Generation).

## Project Structure

```
├── app.py                 # Main Flask application
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
└── college_agent/       # Agent implementation
    ├── .env             # Environment configuration
    ├── agent.py         # AI agent setup
    └── prompts.py       # Agent instruction prompts
```

## Features

- AI-powered chat assistant for college-related queries
- Session-based conversations
- RAG-based information retrieval
- RESTful API endpoints

## Prerequisites

- Python 3.13+
- Google Cloud account
- Vertex AI enabled
- RAG corpus set up in Vertex AI
- Google Cloud CLI installed

## Environment Variables

Create a `.env` file with the following configurations:

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
RAG_CORPUS=projects/{project-id}/locations/{location}/ragCorpora/{corpus-id}
```

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python app.py
```

## API Endpoints

### Start Session
```bash
POST /start_session
{
    "username": "user123",
    "session_name": "session1"
}
```

### Ask Question
```bash
POST /ask
{
    "username": "user123",
    "session_name": "session1",
    "question": "Tell me about college admissions"
}
```

### End Session
```bash
POST /end_session
{
    "username": "user123",
    "session_name": "session1"
}
```

## Deployment to Google Cloud Run

1. Authenticate with Google Cloud:
```bash
gcloud auth login
gcloud config set project your-project-id
```

2. Build and deploy using Cloud Run:
```bash
gcloud run deploy college-agent \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --env-vars-file .env
```

3. Configuration options:
```bash
gcloud run services update college-agent \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300 \
  --concurrency 80
```

## Docker Build

Build the image locally:
```bash
docker build -t college-agent .
```

Run locally:
```bash
docker run -p 5000:5000 \
  --env-file .env \
  college-agent
```

## Testing

Test the deployed service:

```bash
# Get service URL
export SERVICE_URL=$(gcloud run services describe college-agent --format 'value(status.url)')

# Start a session
curl -X POST "${SERVICE_URL}/start_session" \
  -H "Content-Type: application/json" \
  -d '{"username":"test","session_name":"session1"}'

# Ask a question
curl -X POST "${SERVICE_URL}/ask" \
  -H "Content-Type: application/json" \
  -d '{"username":"test","session_name":"session1","question":"Tell me about admissions"}'
```

## Monitoring

Monitor your deployment:
```bash
# View logs
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=college-agent" --limit 50

# Check service status
gcloud run services describe college-agent
```

## Security Considerations

- Use service accounts with minimal permissions
- Enable Cloud Run authentication when needed
- Secure environment variables
- Implement rate limiting
- Monitor API usage

## Troubleshooting

Common issues and solutions:

1. Connection errors:
   - Check environment variables
   - Verify Vertex AI API is enabled
   - Confirm RAG corpus exists

2. Memory issues:
   - Increase Cloud Run instance memory
   - Optimize batch sizes
   - Monitor memory usage

3. Timeouts:
   - Adjust Cloud Run timeout settings
   - Optimize query processing
   - Consider async processing for long operations
