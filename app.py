from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# @app.route('/success/<text><language>')
# def success(text):
#    return 'welcome %s' % text + 'sdhfbsd'

@app.route('/convert',methods = ['POST'])
def convert():
    if request.method == 'POST':
        ttstext = request.form.get('ttstext')
        languageselect = request.form.get('languageselect')
        voiceselect = request.form.get('voiceselect')
        voicestyleselect = request.form.get('voicestyleselect')
        #   return redirect(url_for('',text = ttstext))
        return render_template('index.html', ttstext=ttstext,languageselect=languageselect,voiceselect=voiceselect,voicestyleselect=voicestyleselect)


if __name__ == "__main__":
    app.run(debug = True)
