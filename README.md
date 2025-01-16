# AI_Project



Welcome to the Travel Recommendation App EASYBOOK, a smart application for discovering hotels, restaurants, and tourist attractions, while also interacting with an AI-powered chatbot for travel assistance.

---

## Features

- **Search and Recommendation**: Get recommendations for hotels, restaurants, or tourist attractions near your desired destination.
- **Interactive Maps**: Visualize the recommended places on an interactive map using Folium.
- **AI Chatbot**: Ask travel-related questions to an AI-powered chatbot integrated with Azure OpenAI.
- **Photos and Details**: View photos, ratings, and addresses of recommended places.

---

## Tech Stack

- **Frontend**: Streamlit for a sleek and interactive user interface.
- **Backend**:
  - Google Places API for fetching travel recommendations.
  - Azure OpenAI for chatbot interaction.
- **Programming Language**: Python.
- **Libraries**:
  - `requests` for API communication.
  - `folium` for interactive maps.
  - `streamlit` for web application development.

---

## Installation and Setup

### Prerequisites

- Python 3.7 or higher installed.
- API keys for:
  - Google Places API.
  - Azure OpenAI (GPT-35-Turbo or equivalent deployment).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/travel-recommendation-app.git
   cd travel-recommendation-app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your API keys:
   - Open `app.py`.
   - Replace the placeholders for `GOOGLE_PLACES_API_KEY` and `AZURE_API_KEY` with your API keys.

5. Run the application:
   ```bash
   streamlit run app.py
   ```

6. Open your browser and navigate to `http://localhost:8501` to use the app.

---

## Usage Guide

1. **Search Recommendations**:
   - Enter a destination.
   - Adjust the minimum rating and search radius.
   - Choose between hotels, restaurants, or tourist attractions.
   - Click on "Rechercher 🔍" to get recommendations displayed on an interactive map and a list below.

2. **Chatbot Assistance**:
   - Enter your query in the "ChatBot Azure" section.
   - Receive AI-powered responses to your travel-related questions.

---
