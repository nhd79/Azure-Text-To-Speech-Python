import json
import os
import random
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import azure.cognitiveservices.speech as speechsdk
from flask import Flask, request, render_template, url_for
app = Flask(__name__)


def textToSpeech(ttstext, languageselect, voiceselect):
    # config_file_name = "config_file_dev.json"

    # with open(config_file_name, 'r') as json_data_file:
    #     configuration = json.load(json_data_file)

    # speech_key = configuration["speech_api"]["speech_key"]
    # service_region = configuration["speech_api"]["service_region"]

    # speech_key = os.environ.get('speech_key')
    # service_region = os.environ.get('service_region')
    speech_key = 'c9b15d97bef94a05bed75b56918e924c'
    service_region = 'eastus'

    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=service_region)

    speech_config.speech_synthesis_language = languageselect

    speech_config.speech_synthesis_voice_name = voiceselect

    dir_name = "static/audio/"

    for item in os.listdir(dir_name):
        if item:
            os.remove(os.path.join(dir_name, item))

    # audio_config = AudioOutputConfig(
    #     filename="static\\audio\\"+str(random.randrange(0, 10000, 1))+".wav")

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
                # audio = url_for('static', filename=item)
                audio = os.path.join(dir_name, item)

        return render_template('index.html', audio=audio, ttstext=ttstext, languageselect=languageselect)


if __name__ == "__main__":
    # app.run(debug=True, port=33507) # dev
    app.run()
