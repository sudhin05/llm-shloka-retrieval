const gurus = {
  "vashista": {
    name: "Rishi Vashista",
    image: "images/Rishi_vashista.png",
    intro: "I am Vashistha, the enlightened guide who holds the wisdom of infinite universes. As the royal sage of kings and the preserver of Sanatana Dharma, I illuminate paths of righteousness and self-realization"
  },
  "vishwamitra": {
    name: "Rishi Vishwamitra",
    image: "images/Rishi_vishwamitra.png",
    intro: "I am Vishwamitra, the seeker of the ultimate truth and the creator of the sacred Gayatri Mantra. Known as the sage who traversed from being a king to achieving the title of Brahmarshi, I stand as a testament to perseverance and divine will."
  },
  "atri":{
    name: "Rishi Atri",
    image: "images/Rishi_atri.png",
    intro: "I am Atri, the seer of divine balance and harmony, entrusted with the sacred task of preserving cosmic equilibrium. My vision encompasses all realms, and my words are a reflection of the eternal Vedas"
  },
  "bharadvaja":{
    name: "Rishi Bharadvaja",
    image: "images/Rishi_bharadvaja.png",
    intro: "I am Bharadwaja, the sage of supreme intellect and the knower of sciences. My focus bridges spiritual wisdom and worldly disciplines, uniting the earthly and the divine into one profound teaching"
  },
  "jamadagni":{
    name: "Rishi Jamadagni",
    image: "images/Rishi_jamadagni.png",
    intro: "I am Jamadagni, the sage who pierces illusion with sacred wisdom and divine power. I have fostered a balance between strength and spirituality, teaching the way of karmic detachment and cosmic knowledge"
  },
  "gautama":{
    name: "Rishi Gautama",
    image: "images/Rishi_gautama.png",
    intro: "I am Gautama, the unshakable guide in truth and penance. With an unyielding focus on ascetic discipline and moral justice, I have offered the light of divine knowledge to those lost in darkness"
  },
  "kashyapa":{
    name: "Rishi Kashyapa",
    image: "images/Rishi_kashyapa.png",
    intro: "I am Kashyapa, the progenitor of divine creation and the seer who bridges realms of gods, mortals, and celestial beings. My role is that of a cosmic architect, ever-focused on nurturing harmony in the universe."
  }

};

let selectedGuru = null;

function populateGurus() {
  const gurusContainer = document.querySelector(".gurus");
  Object.keys(gurus).forEach(key => {
    const guru = gurus[key];
    const guruCard = document.createElement("div");
    guruCard.classList.add("guru-card");
    guruCard.setAttribute("data-guru", key);

    guruCard.innerHTML = `
      <img src="${guru.image}" alt="${guru.name}">
      <h3>${guru.name}</h3>
    `;

    guruCard.addEventListener("click", () => selectGuru(key));
    gurusContainer.appendChild(guruCard);
  });
}

function selectGuru(guruKey) {
  selectedGuru = guruKey;
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML = `
    <div class="message bot">${gurus[guruKey].intro}</div>
  `;


  // Enable chat input
  document.getElementById("user-input").disabled = false;
  document.querySelector("button").disabled = false;
}

document.getElementById("chat-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const userInput = document.getElementById("user-input").value;

  if (!selectedGuru) {
    alert("Please select a guru first!");
    return;
  }

  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div class="message user">${userInput}</div>`;
  document.getElementById("user-input").value = "";

  try {
    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userInput, guru: selectedGuru })
    });

    if (!response.ok) throw new Error("Failed to fetch the response.");
    const data = await response.json();
    chatBox.innerHTML += `<div class="message bot">${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (error) {
    chatBox.innerHTML += `<div class="message bot">An error occurred: ${error.message}</div>`;
  }
});

populateGurus();
