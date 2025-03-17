# 🎼 StoryToMidiConversion  
Convert stories into **MIDI music** using LLMs, CSV files, and Python.  
A project from the **AI-Sabotage Lab 2025** at *La Salle – Master of Digital Arts & Creative Tech*.

## 📌 Overview  
This project allows you to transform a **story** into a **MIDI composition**, where each word is mapped to a musical note with **velocity and duration**.  
Using **LLMs** for interpretation and **Python** for conversion. 

---

## 🚀 Usage  

### 1️⃣ Generate a CSV Table 🎶  
Use your **favorite LLM** to interpret your story, assigning:  
- **A note** (e.g., `C4`, `G#3`)  
- **A duration** (in milliseconds, e.g., `400`, `800`)  
- **A velocity** (MIDI intensity, `0-127`)  

You can use the structured **LLM prompt** below to generate the CSV file:  

---

### 🎶 LLM Prompt: Story to MIDI Interpretation  

#### **📝 Task**  
Convert a given story into a **MIDI-compatible CSV file**, where each word is assigned a **single musical note** with a specific **duration (ms) and velocity (0-127)**.  

#### **🎼 Rules & Requirements**  

**1️⃣ Musical Interpretation**  
- Assign **each word** a note from an **appropriate key**.  
- The **key signature** should change based on dramatic moments.  
- Use a **mix of rising, falling, and jumping melodies** to avoid monotony.  

**2️⃣ Dynamic Note Assignment**  
- **Higher notes** → excitement, action, screams (e.g., *"WAMM!!!"*, *"Help!"*).  
- **Lower notes** → darkness, calm, suspense (e.g., *"hole"*, *"terrible"*).  
- Vary between **steps (small jumps), leaps (large jumps), and repetitions**.  

**3️⃣ Duration (Note Length in Milliseconds)**  
- Short words / quick actions → `300-400 ms`  
- Important, meaningful words → `600-800 ms`  
- Extreme emphasis (*e.g., shock, screams*) → `1000+ ms`  

**4️⃣ Velocity (Attack Strength, 0-127)**  
- Strong accents → **90-110** (*"NOW!"*, *"WAMM!!!"*)  
- Soft words → **50-70** (*"said"*, *"the"*, *"and"*)  
- Neutral dynamics → **70-90** (*for regular words*)  

---

#### **📌 Example Output as CSV**  

```csv
word,note,duration,velocity  
"Who",D4,400,70  
"is",E4,300,75  
"afraid",A4,600,100  
"of",G4,400,80  
"Mrs",F4,500,85  
"Wolf?",D4,800,110  
```

✅ **Make sure the output strictly follows these rules.**  
❌ **Avoid random quotation marks or incorrect formatting.**  

---

### 2️⃣ Convert CSV to MIDI 🎼  
Run the `midiConvert.py` script to convert your CSV into a MIDI file.  

📌 **Steps:**  
1. Open your **Python editor** (e.g., **PyCharm, VS Code**).  
2. Install the required dependency:  
   ```bash
   pip install mido
   ```
3. Run the script, linking to your **generated `.csv` file**:  
   ```
   INPUT_TABLE = "yourGeneratedCsv-File.csv" #full path to file
   ```
4. The **MIDI file** will be created in your directory.  

---

### 3️⃣ Use the MIDI File 🎨🔊  
Now that you have a **MIDI file**, you can:  
🎵 **Play it in a DAW** like Ableton Live or FL Studio.  
🎨 **Generate visuals** using Processing or TouchDesigner.  

**Have FUN!** 😃  

---

## ✉️ Contact  
For questions, reach out to **Tim** from class - if you know you know :D.  

---
