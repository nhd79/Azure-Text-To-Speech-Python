# import env # local env file
import os
import random
# import xml.etree.ElementTree as ET
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, SpeechRecognizer, AudioDataStream, ResultReason, CancellationReason
from azure.cognitiveservices.speech.audio import AudioConfig
from flask import Flask, request, render_template
app = Flask(__name__)

def speechConfig():
    speech_key = os.environ.get('speech_key')
    service_region = os.environ.get('service_region')

    return SpeechConfig(
        subscription=speech_key, region=service_region)

def textToSpeech(ttstext, languageselect, voiceselect):
    speech_config = speechConfig()
    speech_config.speech_synthesis_language = languageselect
    speech_config.speech_synthesis_voice_name = voiceselect

    speech_synthesizer = SpeechSynthesizer(
            speech_config=speech_config, audio_config=None)

    dir_name = "static/audio/"

    for item in os.listdir(dir_name):
        if item:
            os.remove(os.path.join(dir_name, item))

    result = speech_synthesizer.speak_text_async(ttstext).get()

    stream = AudioDataStream(result)
    stream.save_to_wav_file(
        "static/audio/"+str(random.randrange(0, 10000, 1))+".wav")

def speechToText(audio_file_path, languageselect):
    speech_config = speechConfig()

    audio_config = AudioConfig(filename=audio_file_path)

    speech_recognizer = SpeechRecognizer(speech_config=speech_config, language=languageselect, audio_config=audio_config)
    result = speech_recognizer.recognize_once()

    # Check the result
    if result.reason == ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        ttstext = request.form.get('ttstext')
        languageselect = request.form.get('languageselect')
        voiceselect = request.form.get('voiceselect')
        # voicestyleselect = request.form.get('voicestyleselect')

        textToSpeech(ttstext, languageselect, voiceselect)

        dir_name = "static/audio/"

        for item in os.listdir(dir_name):
            if item:
                audio = os.path.join(dir_name, item)

        return render_template('index.html', audio=audio, ttstext=ttstext, selectedLang=languageselect, selectedVoice=voiceselect)

@app.route('/totext', methods=['POST'])
def totext():
    if request.method == 'POST':
        languageselect = request.form.get('languageselect')
        audio_file_path = "static/audio/5901.wav"

        result = speechToText(audio_file_path, languageselect)

        return render_template('index.html', audio=audio_file_path, ttstext=result, selectedLang=languageselect)

if __name__ == "__main__":
    # app.run(debug=True) # dev
    app.run()
