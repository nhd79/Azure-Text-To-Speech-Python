import json
import os
import random
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import azure.cognitiveservices.speech as speechsdk
from flask import Flask, request, render_template, redirect, url_for, session
app = Flask(__name__)
used = 0


def textToSpeech(ttstext, languageselect, voiceselect, voicestyleselect):
    config_file_name = "config_file_dev.json"

    with open(config_file_name, 'r') as json_data_file:
        configuration = json.load(json_data_file)

    # Speech SDK
    speech_key = configuration["speech_api"]["speech_key"]
    service_region = configuration["speech_api"]["service_region"]

    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=service_region)

    speech_config.speech_synthesis_language = languageselect

    speech_config.speech_synthesis_voice_name = voiceselect

    dir_name = "static/"
    audio = os.listdir(dir_name)

    for item in audio:
        if item.endswith(".wav"):
            os.remove(os.path.join(dir_name, item))

    audio_config = AudioOutputConfig(filename="static\\"+str(random.randrange(0, 100, 1))+".wav")

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)

    text = ttstext

    speech_synthesizer.speak_text_async(text).get()


@app.route("/")
def index():
    if used == 1:
        dir_name = "static/"
        audio = os.listdir(dir_name)

        for item in audio:
            if item.endswith(".wav"):
                audio = os.path.join(dir_name, item)
                
        return render_template('index.html', audio=audio)
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    if request.method == 'POST':
        global used
        used = 1

        ttstext = request.form.get('ttstext')
        languageselect = request.form.get('languageselect')
        voiceselect = request.form.get('voiceselect')
        voicestyleselect = request.form.get('voicestyleselect')

        textToSpeech(ttstext, languageselect, voiceselect, voicestyleselect)
        # return render_template('index.html', audio="1")
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
