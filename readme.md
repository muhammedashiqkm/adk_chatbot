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