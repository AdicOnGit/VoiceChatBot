import gtts
import io
from pydub.audio_segment import AudioSegment
from pydub.playback import play

def text_to_audio(text, language):
    try:
        if text.strip() != "":
            print("Thinking.......")
            tts = gtts.gTTS(text, lang=language)
            mp3_fp = io.BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            audio = AudioSegment.from_file(mp3_fp, format="mp3")
            print(text)
            play(audio)
    except Exception as e:
        print(f"Error generating audio: {e}")

