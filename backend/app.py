from dotenv import load_dotenv
from groclake.modellake import ModelLake
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

<<<<<<< HEAD
# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/chat": {"origins": "http://127.0.0.1:8080"}})

# Load environment variables
load_dotenv()
=======
app = Flask(__name__)
CORS(app)


load_dotenv()

>>>>>>> f6a2ac14fb56620a714d5c212080e237c45a8baf
os.environ['GROCLAKE_API_KEY'] = os.getenv('GROCLAKE_API_KEY')
os.environ['GROCLAKE_ACCOUNT_ID'] = os.getenv('GROCLAKE_ACCOUNT_ID')

# Initialize ModelLake
model_lake = ModelLake()

<<<<<<< HEAD
# Guru data
GURUS = {
    "vashista": {
        "name": "Rishi Vashista",
        "intro": "I am Vashistha, the enlightened guide who holds the wisdom of infinite universes. As the royal sage of kings and the preserver of Sanatana Dharma, I illuminate paths of righteousness and self-realization.",
        "expertise": " Dharma, ethics, royal advice (rajadharma), yoga, spirituality, meditation, Vedic rituals, divine knowledge, celestial wisdom",
        "image": "frontend/images/Rishi_vashista.png"
    },
    "vishwamitra": {
        "name": "Rishi Vishwamitra",
        "intro": "I am Vishwamitra, the seeker of the ultimate truth and the creator of the sacred Gayatri Mantra. Known as the sage who traversed from being a king to achieving the title of Brahmarshi, I stand as a testament to perseverance and divine will.",
        "expertise": " Meditation, mantras, warfare strategy, spiritual transformation, creation of cosmic energies, Gayatri Mantra, celestial weaponry, ascetic practices",
        "image": "frontend/images/Rishi_vishwamitra.png"
    },
    "atri": {
        "name": "Rishi Atri",
        "intro": "I am Atri, the seer of divine balance and harmony, entrusted with the sacred task of preserving cosmic equilibrium. My vision encompasses all realms, and my words are a reflection of the eternal Vedas.",
        "expertise": "Spiritual equilibrium, cosmic cycles, sacred hymns, Vedic wisdom, meditation, creation of celestial beings, devotion, metaphysical knowledge",
        "image": "frontend/images/Rishi_atri.png"
    },
    "bharadvaja": {
        "name": "Rishi Bharadvaja",
        "intro": "I am Bharadwaja, the sage of supreme intellect and the knower of sciences. My focus bridges spiritual wisdom and worldly disciplines, uniting the earthly and the divine into one profound teaching.",
        "expertise": "Medicine (Ayurveda), military strategy, Vedic knowledge, architecture (Vastu Shastra), profound intellect, divine invocation, spiritual science",
        "image": "frontend/images/Rishi_bharadvaja.png"
    },
    "gautama": {
        "name": "Rishi Gautama",
        "intro": "I am Gautama, the unshakable guide in truth and penance. With an unyielding focus on ascetic discipline and moral justice, I have offered the light of divine knowledge to those lost in darkness.",
        "expertise": "Law (justice), morality, metaphysical awareness, ascetic life, self-purification, penance (tapasya), meditation, Vedic teachings, spiritual guidance",
        "image": "frontend/images/Rishi_gautama.png"
    },
    "jamadagni": {
        "name": "Rishi Jamadagni",
        "intro": "I am Jamadagni, the sage who pierces illusion with sacred wisdom and divine power. I have fostered a balance between strength and spirituality, teaching the way of karmic detachment and cosmic knowledge.",
        "expertise": "Detachment, karmic balance, martial skills, Vedic wisdom, family dharma, penance, divine insight, celestial invocation",
        "image": "frontend/images/Rishi_jamadagni.png"
    },
    "kashyapa": {
        "name": "Rishi Kashyapa",
        "intro": "I am Kashyapa, the progenitor of divine creation and the seer who bridges realms of gods, mortals, and celestial beings. My role is that of a cosmic architect, ever-focused on nurturing harmony in the universe.",
        "expertise": "Creation, cosmology, progeny (lineages), metaphysical connections, balance of nature, rituals, divine order, cosmic energy alignment",
        "image": "frontend/images/Rishi_kashyapa.png"
    },
}

# Generate response using ModelLake
def get_response(conversation):
    try:
        response = model_lake.chat_complete({"messages": conversation, "token_size": 3000
        })
        return response.get('answer', "I'm sorry, I couldn't process that.")
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message')
        selected_guru = data.get('guru')

        if not user_message or not selected_guru:
            return jsonify({"response": "Invalid input."}), 400

        # Validate guru selection
        if selected_guru not in GURUS:
            return jsonify({"response": "Invalid guru selected."}), 400

        # Guru-specific conversation context
        guru = GURUS[selected_guru]
        print(selected_guru)
        conversation = [
            {"role": "system", "content": f"You are {guru['name']}. {guru['intro']} Your expertise is in {guru['expertise']}."},
            {"role": "user", "content": user_message}
        ]

        # Generate response
        response = get_response(conversation)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"response": f"An error occurred: {str(e)}"}), 500
=======
def get_response(user_input):
    """Generates a spiritual response based on the user's query."""
    try:
        # Define the conversation context
        conversation = [
            {"role": "system", "content": "You are a spiritual guide well-versed in the Bhagavad Gita and the Yoga Sutras. Provide meaningful and thoughtful guidance to the user."},
            {"role": "user", "content": user_input}
        ]
        
        # Generate response
        response = model_lake.chat_complete({"messages": conversation, "max_tokens": 3000})
        return response.get('answer', "I'm sorry, I couldn't process that.")
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    if not user_message:
        return jsonify({"response": "I didn't receive any message."})

    bot_reply = get_response(user_message)
    return jsonify({"response": bot_reply})
>>>>>>> f6a2ac14fb56620a714d5c212080e237c45a8baf

if __name__ == '__main__':
    app.run(debug=True)
