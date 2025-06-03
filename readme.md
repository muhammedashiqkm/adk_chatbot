# 🤖 College Course Recommendation Agent with Google ADK & Vertex RAG

This project uses Google’s Agent Development Kit (ADK) with the Vertex AI RAG Engine to recommend courses based on a student's interest survey.

---

## ✅ Prerequisites

1. A **Google Cloud Platform (GCP)** account.
2. Billing enabled for your project.
3. Google Cloud CLI installed: https://cloud.google.com/sdk/docs/install
4. Python 3.9+ and `virtualenv` or `venv`.

---

## 🛠️ Step 1: Create a Google Cloud Project

```bash
gcloud projects create collegeagent-458307 --name="College Agent Project"
```

Set it as your active project:

```bash
gcloud config set project collegeagent-458307
```

---

## 💳 Step 2: Enable Billing

1. Go to: https://console.cloud.google.com/billing
2. Link your billing account to the project `collegeagent-458307`.

You can also do it via CLI:

```bash
gcloud beta billing projects link collegeagent-458307 --billing-account=YOUR_BILLING_ACCOUNT_ID
```

To find your billing account ID:

```bash
gcloud beta billing accounts list
```

---

## 📦 Step 3: Enable Required APIs

```bash
gcloud services enable aiplatform.googleapis.com \
                        discoveryengine.googleapis.com \
                        storage.googleapis.com \
                        cloudbuild.googleapis.com
```

---

## 🧠 Step 4: Upload RAG Corpus to Vertex AI RAG Engine

### 1. Create a Google Cloud Storage bucket

```bash
gsutil mb -l us-central1 gs://collegeagent-rag-corpus
```

### 2. Upload your documents to the bucket

```bash
gsutil cp path/to/documents/* gs://collegeagent-rag-corpus/
```

### 3. Create the RAG Corpus in Vertex

You can do this via the console or Vertex API.

#### a. Using Console (Recommended):

1. Visit: https://console.cloud.google.com/vertex-ai/rag/corpora
2. Click "Create Corpus"
3. Select your project and location (`us-central1`)
4. Choose your uploaded files in the storage bucket
5. Once created, copy the full RAG corpus ID path, e.g.  
   ```
   projects/320796335529/locations/us-central1/ragCorpora/6917529027641081856
   ```

---

## 🔑 Step 5: Set Up Environment Variables

Create a `.env` file and add the following:

```env
# Use Vertex AI as the backend
GOOGLE_GENAI_USE_VERTEXAI=1

# Vertex backend config
GOOGLE_CLOUD_PROJECT=collegeagent-458307
GOOGLE_CLOUD_LOCATION=us-central1

# Your created corpus path
RAG_CORPUS=projects/320796335529/locations/us-central1/ragCorpora/6917529027641081856
```

---

## 🧪 Step 6: Run Your Agent

Install dependencies and run:

```bash
pip install -r requirements.txt
source .env
python main.py
```

---

## 🧼 Optional: Clean Up Resources

```bash
gcloud storage rm -r gs://collegeagent-rag-corpus
gcloud projects delete collegeagent-458307
```

---

## 🧾 Notes

- If you use the RAG Engine, ensure your documents are in `.txt`, `.pdf`, or supported formats.
- RAG Engine is only available in select regions like `us-central1`.

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
