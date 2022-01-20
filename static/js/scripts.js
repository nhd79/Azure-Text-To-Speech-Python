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

// Change button lang
document.getElementById("languageselect").addEventListener("change", (e) => {
  changeVoices(dataVoice, languageselect, voiceselect, selectedVoice);
  if (languageselect.value === "vi-VN") {
    document.getElementById("submit").innerHTML = "Chuyển đổi";
    document.getElementById("sample").innerHTML = "Ví dụ";
    document.getElementById("clear").innerHTML = "Xóa";
  } else {
    document.getElementById("submit").innerHTML = "Convert";
    document.getElementById("sample").innerHTML = "Sample";
    document.getElementById("clear").innerHTML = "Clear";
  }
});

// Sample button
document.getElementById("sample").addEventListener("click", (e) => {
  if (languageselect.value === "vi-VN")
    document.getElementById("ttstext").value =
      "Xin chào, chúc bạn một ngày tốt lành.";
  else document.getElementById("ttstext").value = "Hello from the other side.";
});

// Clear button
document.getElementById("clear").addEventListener("click", (e) => {
  document.getElementById("ttstext").value = "";
});
