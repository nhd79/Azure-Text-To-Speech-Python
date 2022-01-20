function changeVoices(data, languageselect, voiceselect, selectedVoice) {
  while (voiceselect.options.length > 0) {
    voiceselect.remove(0);
  }

  for (let i = 0; i < data.length; i++) {
    let obj = data[i];
    if (languageselect.value === obj["language-value"]) {
      if (obj["value"] === selectedVoice)
        voiceselect.add(
          new Option(obj["voice"], obj["value"], true, true),
          undefined
        );
      else {
        voiceselect.add(new Option(obj["voice"], obj["value"]), undefined);
      }
    }
  }
}
export { changeVoices };
