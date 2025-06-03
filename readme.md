More actions

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
@@ -178,4 +316,4 @@ Common issues and solutions:
3. Timeouts:
   - Adjust Cloud Run timeout settingsAdd commentMore actions
   - Optimize query processing
   - Consider async processing for long operations
   - Consider async processing for long operations
