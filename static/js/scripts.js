import dataLanguage from "../json/languages.json" assert { type: "json" };
import dataVoice from "../json/voices.json" assert { type: "json" };
import { changeLanguages } from "./languages.js";
import { changeVoices } from "./voices.js";

let languageselect = document.getElementById("languageselect");
let voiceselect = document.getElementById("voiceselect");

changeLanguages(dataLanguage, languageselect, selectedLang);

document.onload = changeVoices(
  dataVoice,
  languageselect,
  voiceselect,
  selectedVoice
);
document
  .getElementById("languageselect")
  .addEventListener("change", (e) =>
    changeVoices(dataVoice, languageselect, voiceselect, selectedVoice)
  );

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

      if (document.getElementById("ttstext").value == "")
        document.getElementById("ttstext").value = "Hello from the other side.";

      break;

    case "en-GB":
      removeOptions(voiceselect);

      addOption("Libby (Neural)", "en-GB-LibbyNeural");
      addOption("Ryan (Neural)", "en-GB-RyanNeural");
      addOption("Sonia (Neural)", "en-GB-SoniaNeural");

      if (document.getElementById("ttstext").value == "")
        document.getElementById("ttstext").value = "Hello from the other side.";

      break;

    default:
      removeOptions(voiceselect);

      addOption("HoaiMy (Neural) - Hoài My", "vi-VN-HoaiMyNeural");
      addOption("NamMinh (Neural) - Nam Minh", "vi-VN-NamMinhNeural");

      if (document.getElementById("ttstext").value == "")
        document.getElementById("ttstext").value =
          "Xin chào, chúc bạn một ngày tốt lành.";
  }
}
function addOption(text, value) {
  voiceselect.add(new Option(text, value), undefined);
}
