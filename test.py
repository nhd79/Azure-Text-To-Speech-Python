import xml.etree.ElementTree as ET

speak = ET.Element('speak')
voice = ET.SubElement(speak, 'voice')
speak.set('xmlns','https://www.w3.org/2001/10/synthesis')
speak.set('version','1.0')
speak.set('xml:lang',languageselect)
voice.set('name',voiceselect)
voice.text = ttstext

ET.indent(speak)
data = ET.tostring(speak, encoding="unicode")
file = open("ssml.xml", "w")
file.write(data)


# ET.register_namespace('', "https://www.w3.org/2001/10/synthesis")

# tree = ET.parse('ssml.xml')
# speak = tree.getroot()

# # changing a field text
# for voice in speak.iter('voice'):
#     voice.text = ttstext

# # modifying an attribute
# for elem in speak.iter('voice'):
#     elem.set('name', voiceselect)

# tree.write('ssml.xml')

ssml_string = open("ssml.xml", "r").read()

result = speech_synthesizer.speak_ssml_async(ssml_string).get()

