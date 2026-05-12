import time
import sys
import os
from gtts import gTTS
from pygame import mixer

# Color Codes (ANSI Escape Sequences)
GOLD = '\033[38;5;220m'
SOFT_WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

def soul_typing_with_voice(text, color, speed=0.1):
    # 1. Prepare Voice (Speech Generation)
    tts = gTTS(text=text, lang='hi') # Keep lang='hi' for Hindi lyrics
    tts.save("voice.mp3")
    
    # 2. Play Audio
    mixer.init()
    mixer.music.load("voice.mp3")
    mixer.music.play()

    # 3. Type Text (Visual Effect)
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    
    # Wait for the audio to finish playing
    while mixer.music.get_busy():
        time.sleep(0.1)
    
    mixer.quit()
    
    # Cleanup: Remove the temporary file
    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")
    print()

# --- Main Execution ---
print(f"\n{SOFT_WHITE}✨ Connecting to Soul...{RESET}\n")
time.sleep(1)

lyrics = [
    ("Sitare sitare mile hain sitare", GOLD),
    ("Tabhi toh huye hain nazare tumhare", SOFT_WHITE),
    ("O sitare sitare mile hain sitare", GOLD),
    ("Tabhi toh huye hain nazare tumhare", SOFT_WHITE),
    ("Bas tum se milne ki der thi", GOLD),
    ("Tum se milne ki der thi", SOFT_WHITE),
    ("Tum se milne ki der thi", GOLD)
]

for line, color in lyrics:
    soul_typing_with_voice(line, color, speed=0.15)