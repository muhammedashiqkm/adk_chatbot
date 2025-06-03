Okay, here's the content formatted entirely in Markdown, suitable for a GitHub README:Add commentMore actions
More actions

Markdown
# 🤖 College Course Recommendation Agent with Google ADK & Vertex RAG

## 🤖 College Course Recommendation Agent with Google ADK & Vertex RAG

This project leverages Google's Agent Development Kit (ADK) with the Vertex AI RAG Engine to recommend college courses based on a student's interest survey.
This project uses Google’s Agent Development Kit (ADK) with the Vertex AI RAG Engine to recommend courses based on a student's interest survey.

---

### ✅ Prerequisites
## ✅ Prerequisites

* A **Google Cloud Platform (GCP)** account.
* **Billing enabled** for your project.
* **Google Cloud CLI** installed: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
* **Python 3.9+** and `virtualenv` or `venv`.
1. A **Google Cloud Platform (GCP)** account.
2. Billing enabled for your project.
3. Google Cloud CLI installed: https://cloud.google.com/sdk/docs/install
4. Python 3.9+ and `virtualenv` or `venv`.

---

### 🛠️ Step 1: Create a Google Cloud Project

First, create your GCP project.
## 🛠️ Step 1: Create a Google Cloud Project

```bash
gcloud projects create collegeagent-458307 --name="College Agent Project"
Then, set it as your active project for all subsequent commands:
```

Bash
Set it as your active project:

```bash
gcloud config set project collegeagent-458307
💳 Step 2: Enable and Link Billing
You need to link a billing account to your project to use Google Cloud services.
```

---

Go to Billing: Navigate to the Google Cloud Billing page.
Create a Billing Account: If you don't have one, select "Create billing account" and follow the prompts.
Link Billing Account to Project:
## 💳 Step 2: Enable Billing

If your project collegeagent-458307 isn't linked, select "Link a billing account" and choose your new or existing billing account.
If it's already linked, go to "Manage billing accounts," select your billing account, and check the project details. You can click the three dots next to your project to change the billing account if needed.
Alternatively, you can link it via the CLI:
1. Go to: https://console.cloud.google.com/billing
2. Link your billing account to the project `collegeagent-458307`.

Bash
You can also do it via CLI:

```bash
gcloud beta billing projects link collegeagent-458307 --billing-account=YOUR_BILLING_ACCOUNT_ID
To find your billing account ID:
```

Bash
To find your billing account ID:

```bash
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
---

- Python 3.13+
- Google Cloud account
- Vertex AI enabled
- RAG corpus set up in Vertex AI
- Google Cloud CLI installed
## 📦 Step 3: Enable Required APIs

## Environment Variables
```bash
gcloud services enable aiplatform.googleapis.com \
                        discoveryengine.googleapis.com \
                        storage.googleapis.com \
                        cloudbuild.googleapis.com
```

Create a `.env` file with the following configurations:
---

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
RAG_CORPUS=projects/{project-id}/locations/{location}/ragCorpora/{corpus-id}
```
## 🧠 Step 4: Upload RAG Corpus to Vertex AI RAG Engine

## Local Development
### 1. Create a Google Cloud Storage bucket

1. Install dependencies:
```bash
pip install -r requirements.txt
gsutil mb -l us-central1 gs://collegeagent-rag-corpus
```

2. Run the Flask application:
### 2. Upload your documents to the bucket

```bash
python app.py
gsutil cp path/to/documents/* gs://collegeagent-rag-corpus/
```

## API Endpoints
### 3. Create the RAG Corpus in Vertex

### Start Session
```bash
POST /start_session
{
    "username": "user123",
    "session_name": "session1"
}
```
You can do this via the console or Vertex API.

### Ask Question
```bash
POST /ask
{
    "username": "user123",
    "session_name": "session1",
    "question": "Tell me about college admissions"
}
```
#### a. Using Console (Recommended):

### End Session
```bash
POST /end_session
{
    "username": "user123",
    "session_name": "session1"
}
```
1. Visit: https://console.cloud.google.com/vertex-ai/rag/corpora
2. Click "Create Corpus"
3. Select your project and location (`us-central1`)
4. Choose your uploaded files in the storage bucket
5. Once created, copy the full RAG corpus ID path, e.g.  
   ```
   projects/320796335529/locations/us-central1/ragCorpora/6917529027641081856
   ```

## Deployment to Google Cloud Run
---

1. Authenticate with Google Cloud:
```bash
gcloud auth login
gcloud config set project your-project-id
```
## 🔑 Step 5: Set Up Environment Variables

2. Build and deploy using Cloud Run:
```bash
gcloud run deploy college-agent \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --env-vars-file .env
```
Create a `.env` file and add the following:

3. Configuration options:
```bash
gcloud run services update college-agent \
  --memory 2Gi \
  --cpu 2 \
  --timeout 300 \
  --concurrency 80
```
```env
# Use Vertex AI as the backend
GOOGLE_GENAI_USE_VERTEXAI=1

## Docker Build
# Vertex backend config
GOOGLE_CLOUD_PROJECT=collegeagent-458307
GOOGLE_CLOUD_LOCATION=us-central1

Build the image locally:
```bash
docker build -t college-agent .
# Your created corpus path
RAG_CORPUS=projects/320796335529/locations/us-central1/ragCorpora/6917529027641081856
```

Run locally:
```bash
docker run -p 5000:5000 \
  --env-file .env \
  college-agent
```
---

## Testing
## 🧪 Step 6: Run Your Agent

Test the deployed service:
Install dependencies and run:

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
pip install -r requirements.txt
source .env
python main.py
```

## Monitoring
---

## 🧼 Optional: Clean Up Resources

Monitor your deployment:
```bash
# View logs
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=college-agent" --limit 50

# Check service status
gcloud run services describe college-agent
gcloud storage rm -r gs://collegeagent-rag-corpus
gcloud projects delete collegeagent-458307
```

## Security Considerations

- Use service accounts with minimal permissions
- Enable Cloud Run authentication when needed
- Secure environment variables
- Implement rate limiting
- Monitor API usage
---

## Troubleshooting
## 🧾 Notes

Common issues and solutions:
- If you use the RAG Engine, ensure your documents are in `.txt`, `.pdf`, or supported formats.
- RAG Engine is only available in select regions like `us-central1`.

1. Connection errors:
   - Check environment variables
   - Verify Vertex AI API is enabled
   - Confirm RAG corpus exists
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Memory issues:
   - Increase Cloud Run instance memory
   - Optimize batch sizes
   - Monitor memory usage
# College Agent - Sullamussalam Science College Assistant

A Flask-based REST API service that provides an AI assistant for Sullamussalam Science College using Google's Vertex AI and RAG (Retrieval Augmented Generation).
@@ -178,4 +316,4 @@ Common issues and solutions:
3. Timeouts:
   - Adjust Cloud Run timeout settings
   - Adjust Cloud Run timeout settingsAdd commentMore actions
   - Optimize query processing
   - Consider async processing for long operations
   - Consider async processing for long operations
