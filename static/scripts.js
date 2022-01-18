function changeVoice() {
  let languageselect = document.getElementById("languageselect");
  let voiceselect = document.getElementById("voiceselect");

  switch (languageselect.value) {
    case "en-US":
      removeOptions(voiceselect);

      addOption("Jenny (Neural)", "en-US-JennyNeural");
      addOption(
        "Jenny Multilingual (Neural) - Preview",
        "en-US-JennyMultilingualNeural"
      );
      addOption("Guy (Neural)", "en-US-GuyNeural");
      addOption("Amber (Neural)", "en-US-AmberNeural");
      addOption("Ana (Neural)", "en-US-AnaNeural");
      addOption("Aria (Neural)", "en-US-AriaNeural");
      addOption("Ashley (Neural)", "en-US-AshleyNeural");
      addOption("Brandon (Neural)", "en-US-BrandonNeural");
      addOption("Christopher (Neural)", "en-US-ChristopherNeural");
      addOption("Cora (Neural)", "en-US-CoraNeural");
      addOption("Elizabeth (Neural)", "en-US-ElizabethNeural");
      addOption("Eric (Neural)", "en-US-EricNeural");
      addOption("Jacob (Neural)", "en-US-JacobNeural");
      addOption("Michelle (Neural)", "en-US-MichelleNeural");
      addOption("Monica (Neural)", "en-US-MonicaNeural");
      addOption("Sara (Neural)", "en-US-SaraNeural");

      break;

    case "en-GB":
      removeOptions(voiceselect);

      addOption("Libby (Neural)", "en-GB-LibbyNeural");
      addOption("Ryan (Neural)", "en-GB-RyanNeural");
      addOption("Sonia (Neural)", "en-GB-SoniaNeural");

      break;

    default:
      removeOptions(voiceselect);

      addOption("HoaiMy (Neural) - Hoài My", "vi-VN-HoaiMyNeural");
      addOption("NamMinh (Neural) - Nam Minh", "vi-VN-NamMinhNeural");
  }
}
function removeOptions(element) {
  while (element.options.length > 0) {
    element.remove(0);
  }
}
function addOption(text, value) {
  voiceselect.add(new Option(text, value), undefined);
}
