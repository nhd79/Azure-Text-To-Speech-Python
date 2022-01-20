function changeLanguages(data, languageselect, selectedLang) {
  for (let i = 0; i < data.length; i++) {
    let obj = data[i];
    if (obj["value"] === selectedLang)
      languageselect.add(
        new Option(obj["language"], obj["value"], true, true),
        undefined
      );
    else {
      languageselect.add(new Option(obj["language"], obj["value"]), undefined);
    }
  }
}
export { changeLanguages };
