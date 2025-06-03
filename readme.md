
# 🧠 Vertex AI RAG Setup for ADK Chatbot

This guide walks you through the step-by-step process of setting up a Retrieval-Augmented Generation (RAG) pipeline using Google Cloud's Vertex AI, and configuring your environment for a chatbot powered by Google’s Agent Development Kit (ADK).

---

## ✅ Prerequisites

- A Google Account
- Access to [Google Cloud Console](https://console.cloud.google.com/)
- `gcloud` CLI installed

---

## 🪪 Step 1: Sign In to Google Cloud Console

1. Go to [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. Sign in using your Google account.

---

## 🏗️ Step 2: Create a New Project

1. In the top navigation bar, click the project drop-down menu.
2. Click **“New Project”**.
3. Fill in the details:
   - **Project Name**: e.g., `my-open-source-app`
   - **Organization**: Leave as `No organization` if not applicable.
4. Click **“Create”**.

---

## 💳 Step 3: Set Up Billing

1. Navigate to **Billing** in the left sidebar.
2. If you haven’t already:
   - Click **Create Billing Account**.
   - Follow the steps to add a payment method.
3. Link your project to the billing account:
   - In the **Billing** section, go to **Manage Billing Accounts**.
   - Click the three dots (⋮) next to your billing account to find the option to **Change Project** or link the account.

---

## 📚 Step 4: Create RAG Corpus in Vertex AI

1. Enable the **Vertex AI API** from the [API Library](https://console.cloud.google.com/apis/library).
2. Navigate to **Vertex AI** → **Retrieval** → **RAG Engine**.
3. Select **us-central1** as your region.
4. Click **Create Corpus** and fill in the details:
   - **Corpus Name**
   - **Description** (optional)
5. Upload your PDF document(s) from a storage source (e.g., Google Drive).
6. Click **Continue**, then:
   - Choose `textembedding-gecko@003` or `text-embedding-004` as the embedding model.
   - Choose `RagManaged Vector Store`.
7. Click **Create Corpus**.
8. Once created, go to the **Details** tab of your corpus and **copy the Resource name** (e.g.,  
   `projects/your-project-id/locations/us-central1/ragCorpora/your-corpus-id`).

---

## ⚙️ Step 5: Configure `.env` File

Update your `.env` file in the root of your project:

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-gcp-project-id
GOOGLE_CLOUD_LOCATION=us-central1
RAG_CORPUS=projects/your-gcp-project-id/locations/us-central1/ragCorpora/your-corpus-id
```

---

# 🎓 College Agent - Sullamussalam Science College Assistant

A Flask-based REST API service that provides an AI assistant for Sullamussalam Science College using Google's Vertex AI and RAG (Retrieval Augmented Generation).

## 📁 Project Structure

```
├── app.py                 # Main Flask application
├── Dockerfile            # Container configuration
├── requirements.txt      # Python dependencies
└── college_agent/       # Agent implementation
    ├── .env             # Environment configuration
    ├── agent.py         # AI agent setup
    └── prompts.py       # Agent instruction prompts
```

## ✨ Features

- AI-powered chat assistant for college-related queries
- Session-based conversations
- RAG-based information retrieval
- RESTful API endpoints

## ✅ Prerequisites

- Python 3.13+
- Google Cloud account
- Vertex AI enabled
- RAG corpus set up in Vertex AI
- Google Cloud CLI installed

## 🛠 Environment Variables

Create a `.env` file with the following configurations:

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
RAG_CORPUS=projects/{project-id}/locations/{location}/ragCorpora/{corpus-id}
```

## 🧪 Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python app.py
```

## 🌐 API Endpoints

### ▶️ Start Session
```bash
POST /start_session
{
    "username": "user123",
    "session_name": "session1"
}
```

### ❓ Ask Question
```bash
POST /ask
{
    "username": "user123",
    "session_name": "session1",
    "question": "Tell me about college admissions"
}
```

### ⏹ End Session
```bash
POST /end_session
{
    "username": "user123",
    "session_name": "session1"
}
```

## ☁️ Deployment to Google Cloud Run

1. Authenticate with Google Cloud:
```bash
gcloud auth login
gcloud config set project your-project-id
```

2. Build and deploy using Cloud Run:
```bash
gcloud run deploy college-agent   --source .   --region us-central1   --platform managed   --allow-unauthenticated   --env-vars-file .env
```

3. Configuration options:
```bash
gcloud run services update college-agent   --memory 1Gi   --cpu 1   --timeout 300   --concurrency 80
```

## 🐳 Docker Build

Build the image locally:
```bash
docker build -t college-agent .
```

Run locally:
```bash
docker run -p 5000:5000   --env-file .env   college-agent
```

## 🧪 Testing

```bash
export SERVICE_URL=$(gcloud run services describe college-agent --format 'value(status.url)')

curl -X POST "${SERVICE_URL}/start_session"   -H "Content-Type: application/json"   -d '{"username":"test","session_name":"session1"}'

curl -X POST "${SERVICE_URL}/ask"   -H "Content-Type: application/json"   -d '{"username":"test","session_name":"session1","question":"Tell me about admissions"}'
```

## 📊 Monitoring

```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=college-agent" --limit 50
gcloud run services describe college-agent
```

## 🔐 Security Considerations

- Use service accounts with minimal permissions
- Enable Cloud Run authentication when needed
- Secure environment variables
- Implement rate limiting
- Monitor API usage

## 🛠 Troubleshooting

1. **Connection errors**
   - Check environment variables
   - Verify Vertex AI API is enabled
   - Confirm RAG corpus exists

2. **Memory issues**
   - Increase Cloud Run instance memory
   - Optimize batch sizes
   - Monitor memory usage

3. **Timeouts**
   - Adjust Cloud Run timeout settings
   - Optimize query processing
   - Consider async processing for long operations

---

## 🐧 Deployment to Linux Server

### 🚀 Option 1: Docker-Based Deployment (Recommended)

#### ✅ Prerequisites

- Linux server (e.g., Ubuntu 20.04+)
- Docker installed:
```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

#### 📦 Build the Docker Image

```bash
docker build -t college-agent .
```

#### ▶️ Run the Docker Container

```bash
docker run -d -p 5000:5000   --env-file .env   --name college_agent_container   college-agent
```

Access the app at: `http://<your-server-ip>:5000`

---

### 🛠 Option 2: Manual Deployment (No Docker)

#### ✅ Prerequisites

- Python 3.9+ installed on the server
- `pip`, `virtualenv`, and GCP CLI installed

#### 📦 Set up the project:

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
cd /path/to/project
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export $(cat .env | xargs)
```

#### ▶️ Run the Flask App

```bash
python app.py
```

Or use Gunicorn:

```bash
pip install gunicorn
gunicorn app:app --bind 0.0.0.0:5000
```

#### 🔄 Keep the App Running

```bash
nohup gunicorn app:app --bind 0.0.0.0:5000 &
```
