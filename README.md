# Post-Stats-Tracker for LinkedIn
A FastAPI-based integration that tracks the number of likes and reposts on a specified LinkedIn post and sends updates to Telex at regular intervals.

![Telex Logo](https://iili.io/Jcshqe2.md.webp)


📌 Features
✅ Fetches LinkedIn post statistics (likes & reposts).
✅ Sends notifications to Telex at defined intervals.
✅ Configurable update frequency via Telex settings.
✅ Supports CORS for cross-origin API requests.

🛠️ Installation & Setup
1️⃣ Clone the Repository

```sh
git clone https://github.com/telexintegrations/hngx_stage3_telex_integration_linkedin
cd hngx_stage3_telex_integration_linkedin
```
2️⃣ Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

4️⃣ Set Up Environment Variables
Create a .env file in the project root and add:

```ini
LINKEDIN_API_KEY=your_linkedin_api_key
LINKEDIN_API_SECRET=your_linkedin_api_secret
```

🚀 Running the Application Locally

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
API will be available at: http://127.0.0.1:8000

🔗 API Endpoints
Health Check

```http
GET /
```
🔹 Response: {"message":"Post-stats-tracker for Linkedin is working!"}

Get Integration Info
```http
GET /integration.json
```
🔹 Response: Returns Telex-compatible metadata
Fetch LinkedIn Post Stats
```http
POST /fetch-stats
```
📌 How to Use on Telex
1. Go to Telex Dashboard → Add Integration
2. Enter the Integration URL:
```bash
https://hngx-stage3-telex-integration-linkedin.vercel.app/integration.json
```
3. Manage app.
4. Telex will now fetch LinkedIn post stats and send notifications automatically! 🎉

🛠️ Troubleshooting
If Telex doesn’t detect the integration:
✅ Ensure https://your-vercel-app.vercel.app/integration.json is accessible.
✅ Check CORS settings in FastAPI.
✅ Restart FastAPI (vercel --prod after making changes).




