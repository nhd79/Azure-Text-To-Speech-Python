import json
import os
import random
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import azure.cognitiveservices.speech as speechsdk
from flask import Flask, request, render_template, url_for
app = Flask(__name__)


def textToSpeech(ttstext, languageselect, voiceselect):

    speech_key = os.environ.get('speech_key')
    service_region = os.environ.get('service_region')

    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=service_region)

    speech_config.speech_synthesis_language = languageselect

    speech_config.speech_synthesis_voice_name = voiceselect

    dir_name = "static/audio/"

    for item in os.listdir(dir_name):
        if item:
            os.remove(os.path.join(dir_name, item))

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=None)

    result = speech_synthesizer.speak_text_async(ttstext).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file(
        "static/audio/"+str(random.randrange(0, 10000, 1))+".wav")


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        ttstext = request.form.get('ttstext')
        languageselect = request.form.get('languageselect')
        voiceselect = request.form.get('voiceselect')

        textToSpeech(ttstext, languageselect, voiceselect)

        dir_name = "static/audio/"

        for item in os.listdir(dir_name):
            if item:
                audio = os.path.join(dir_name, item)

        return render_template('index.html', audio=audio, ttstext=ttstext, selectedLang=languageselect,selectedVoice=voiceselect)


if __name__ == "__main__":
    # app.run(debug=True) # dev
    app.run()
