import whisper
from googletrans import Translator
from gtts import gTTS
import tempfile


# LOAD WHISPER MODEL

model = whisper.load_model("base")

# TRANSCRIBE AUDIO

def transcribe_audio(audio_file):

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as temp_audio:

            temp_audio.write(audio_file.read())

            temp_audio_path = temp_audio.name

        result = model.transcribe(temp_audio_path)

        return result["text"]

    except Exception as e:

        return f"Error during transcription: {str(e)}"


# TRANSLATE TEXT

def translate_text(text, target_language):

    try:

        translator = Translator()

        translated = translator.translate(
            text,
            dest=target_language
        )

        return translated.text

    except Exception as e:

        return f"Translation Error: {str(e)}"

# TEXT TO SPEECH

def text_to_speech(text, language="en"):

    try:

        tts = gTTS(
            text=text,
            lang=language
        )

        temp_audio = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        tts.save(temp_audio.name)

        return temp_audio.name

    except Exception as e:

        print(f"TTS Error: {str(e)}")

        return None