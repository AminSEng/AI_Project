import streamlit as st 
import requests 
import folium
from streamlit_folium import folium_static

# Clés API
GOOGLE_PLACES_API_KEY = "YOUR_GOOGLE_API_KEY"
AZURE_API_KEY = "YOUR_AZURE_API_KEY"
AZURE_API_URL = "YOUR_AZURE_API_URL"

# Configuration de la page Streamlit
st.set_page_config(page_title="Travel Recommendation App", page_icon="🌍", layout="wide")

# Style CSS
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stTextInput > div > input {
            border: 2px solid #4CAF50;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🌍 Travel Recommendation App 🌍")

# Entrées utilisateur
with st.sidebar:
    st.header("Paramètres de recherche")
    destination = st.text_input("Destination :", "Bali, Indonesia")
    min_rating = st.slider("Note minimale :", 0.0, 5.0, 4.0, step=0.1)
    radius = st.number_input("Rayon de recherche en mètres :", 100, 50000, 3000)

    search_type = st.radio(
        "Que recherchez-vous ?", ("Hotels 🏨", "Restaurants 🍴", "Tourist Attractions ⭐")
    )

# Affichage des recommandations
if st.button("Rechercher 🔍"):
    st.subheader(f"Voici nos recommandations pour {search_type} près de {destination}")

    # Appel à l'API Google Places
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"{search_type} in {destination}",
        "key": GOOGLE_PLACES_API_KEY,
        "radius": radius
    }

    response = requests.get(url, params=params)
    results = response.json()

    if "results" in results and len(results["results"]) > 0:
        map_center = results["results"][0]["geometry"]["location"]
        map = folium.Map(location=[map_center["lat"], map_center["lng"]], zoom_start=13)

        # Ajouter les lieux à la carte
        for place in results["results"]:
            name = place["name"]
            lat = place["geometry"]["location"]["lat"]
            lng = place["geometry"]["location"]["lng"]
            address = place.get("formatted_address", "Adresse non disponible")
            rating = place.get("rating", "Note non disponible")
            popup_info = f"<b>{name}</b><br>Adresse: {address}<br>Note: {rating}"

            folium.Marker([lat, lng], popup=popup_info).add_to(map)

        # Afficher la carte
        folium_static(map)

        # Afficher les détails sous forme de carte avec des photos
        st.subheader("Détails des lieux :")
        for place in results["results"]:
            name = place["name"]
            address = place.get("formatted_address", "Adresse non disponible")
            rating = place.get("rating", "Note non disponible")

            photo_url = None
            if "photos" in place:
                photo_reference = place["photos"][0]["photo_reference"]
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={GOOGLE_PLACES_API_KEY}"

            with st.container():
                st.markdown(f"### {name}")
                st.markdown(f"**Adresse :** {address}")
                st.markdown(f"**Note :** {rating}")
                if photo_url:
                    st.image(photo_url, caption=name, use_column_width=True)
                st.markdown("---")
    else:
        st.error("Aucun résultat trouvé. Veuillez essayer avec une autre destination.")

# ChatBot Azure OpenAI
with st.sidebar:
    st.header("ChatBot Azure 🤖")
    user_question = st.text_input("Votre question :", "")

if user_question:
    st.subheader("ChatBot Azure : Posez vos questions")

    # Appel à l'API Azure
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_API_KEY
    }

    payload = {
        "messages": [
            {"role": "system", "content": "Vous êtes un assistant IA prêt à aider."},
            {"role": "user", "content": user_question}
        ],
        "max_tokens": 200,
        "temperature": 0.7
    }

    try:
        response = requests.post(AZURE_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        bot_response = result['choices'][0]['message']['content']
        st.write(f"### 🤖 Réponse : {bot_response}")
    except Exception as e:
        st.error(f"Erreur avec le ChatBot Azure : {str(e)}")
