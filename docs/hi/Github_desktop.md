---
title: "वर्जन कंट्रोल के साथ शुरुआत करें"
lang: "hi"
---
[होम](./)

# वर्जन कंट्रोल के साथ शुरुआत करें

आप किसी प्रोजेक्ट पर काम कर रहे हैं और ऐसे बदलाव करते हैं जो सब कुछ बिगाड़ देते हैं। आपको याद नहीं कि आपने क्या बदला, और आप चाहते हैं कि आप उस समय पर वापस जा सकें जब सब कुछ ठीक काम कर रहा था। वर्जन कंट्रोल (Version Control) किसी वीडियो गेम के सेव पॉइंट्स की तरह है—हर बार जब आप अपने काम को "कमिट" (commit) करते हैं, तो आप एक रीस्टोर पॉइंट बनाते हैं जिस पर आप हमेशा वापस लौट सकते हैं। [GitHub](https://github.com) आपके सेव पॉइंट्स को क्लाउड में संग्रहीत करता है, ताकि आपका कोड सुरक्षित रूप से बैकअप हो और किसी भी कंप्यूटर से एक्सेस किया जा सके।

## मुख्य अवधारणाएँ

- **Git** - वर्जन कंट्रोल सॉफ़्टवेयर जो आपके कंप्यूटर पर आपकी फ़ाइलों में हुए बदलावों को ट्रैक करता है
- **GitHub** - एक वेबसाइट जो आपके कोड को क्लाउड में संग्रहीत करती है, कोड के लिए Google Drive की तरह
- **GitHub Desktop** - एक ऐप जो कमांड की जगह बटन के ज़रिए Git का उपयोग आसान बनाता है
- **Repository (repo)** - एक प्रोजेक्ट फ़ोल्डर जो आपके सभी बदलावों को ट्रैक करता है

## आपको क्या चाहिए

- Windows, macOS, या Linux कंप्यूटर
- इंटरनेट कनेक्शन
- GitHub अकाउंट के लिए ईमेल पता
- 15-20 मिनट

## चरण 1: एक GitHub अकाउंट बनाएं

- अपना वेब ब्राउज़र खोलें
- [github.com](https://github.com) पर जाएं
- **Sign up** पर क्लिक करें
- अपना ईमेल डालें, एक पासवर्ड बनाएं, और एक यूज़रनेम चुनें
- सत्यापन (verification) के चरण पूरे करें

## चरण 2: GitHub Desktop डाउनलोड करें

- [desktop.github.com](https://desktop.github.com) पर जाएं
- **Download** बटन पर क्लिक करें
- इंस्टॉल करने के लिए डाउनलोड की गई फ़ाइल खोलें

**Windows पर:**
- इंस्टॉलर फ़ाइल पर डबल-क्लिक करें
- GitHub Desktop अपने आप इंस्टॉल होकर खुल जाएगा

**Mac पर:**
- डाउनलोड की गई `.zip` फ़ाइल खोलें
- **GitHub Desktop** को अपने Applications फ़ोल्डर में खींचें (drag करें)
- Applications से GitHub Desktop खोलें

## चरण 3: GitHub Desktop में साइन इन करें

- GitHub Desktop खोलें
- **Sign in to GitHub.com** पर क्लिक करें
- आपका ब्राउज़र खुलेगा—**Authorize desktop** पर क्लिक करें
- GitHub Desktop पर वापस लौटें
- सेटअप पूरा करने के लिए **Finish** पर क्लिक करें

## चरण 4: अपनी पहली Repository बनाएं

- GitHub Desktop में, **Create a New Repository on your Hard Drive** पर क्लिक करें
- फॉर्म भरें:
  - **Name:** `my-first-project` (या कोई भी नाम जो आपको पसंद हो)
  - **Description:** `Learning version control` (वैकल्पिक)
  - **Local Path:** चुनें कि इसे कहाँ सेव करना है (Documents फ़ोल्डर ठीक रहेगा)
  - **Initialize this repository with a README** को चेक करें
- **Create Repository** पर क्लिक करें

## चरण 5: अपना प्रोजेक्ट फ़ोल्डर खोलें

- GitHub Desktop में, मेनू बार में **Repository** पर क्लिक करें
- **Show in Finder** (Mac) या **Show in Explorer** (Windows) चुनें
- आपको अपने प्रोजेक्ट के नाम वाला एक फ़ोल्डर दिखेगा
- इसके अंदर `README.md` नाम की एक फ़ाइल होगी

## चरण 6: अपना पहला बदलाव करें

- `README.md` को किसी भी टेक्स्ट एडिटर (Notepad, TextEdit, या VS Code) में खोलें
- इसकी सामग्री को इससे बदलें:
  ```
  # My First Project

  I'm learning version control with GitHub Desktop.

  ## What I'm Building

  This is a practice project to learn how to:
  - Track changes to my code
  - Create save points (commits)
  - Back up my work to GitHub
  ```
- **File** → **Save** पर क्लिक करें

## चरण 7: अपना पहला Commit (सेव पॉइंट) बनाएं

- GitHub Desktop पर वापस लौटें
- आपको दाईं ओर अपने बदलाव हाइलाइट किए हुए दिखेंगे (हरा = जोड़ा गया, लाल = हटाया गया)
- नीचे बाईं ओर, एक commit संदेश टाइप करें: `Updated README with project description`
- नीले **Commit to main** बटन पर क्लिक करें

## चरण 8: GitHub पर Push करें (क्लाउड में बैकअप लें)

- ऊपर नीले **Publish repository** बटन पर क्लिक करें
- नाम वैसा ही रहने दें
- यदि आप चाहते हैं कि दूसरे लोग इसे देख सकें तो "Keep this code private" को अनचेक करें (वैकल्पिक)
- **Publish Repository** पर क्लिक करें

अब आपका कोड ऑनलाइन बैकअप हो चुका है: `https://github.com/YOUR-USERNAME/my-first-project`

## अगले कदम

- अपनी README फ़ाइल को फिर से बदलें और उन बदलावों को commit करें
- अपने प्रोजेक्ट फ़ोल्डर में एक नई फ़ाइल बनाएं और उसे commit करें
- यह देखने के लिए **History** टैब देखें कि आपका प्रोजेक्ट समय के साथ कैसे विकसित होता है

## समस्या निवारण

- **GitHub में साइन इन नहीं हो पा रहा** - अपना इंटरनेट कनेक्शन जांचें। पहले github.com पर साइन इन करके देखें कि आपकी लॉगिन जानकारी सही काम कर रही है।
- **बदलाव GitHub Desktop में नहीं दिख रहे** - सुनिश्चित करें कि आपने अपनी फ़ाइलें सेव कर ली हैं। **Repository** → **Refresh** पर क्लिक करें या GitHub Desktop को दोबारा शुरू करें।
- **Push "rejected" एरर के साथ विफल हो रहा है** - किसी और ने बदलाव push किए हैं। पहले **Fetch origin** पर क्लिक करें, फिर दोबारा push करने की कोशिश करें।

## वर्कफ़्लो का अवलोकन

- अपनी प्रोजेक्ट फ़ाइलों में बदलाव करें
- GitHub Desktop में बदलाव देखें (हरा = जोड़ा गया, लाल = हटाया गया)
- एक स्पष्ट commit संदेश लिखें और **Commit to main** पर क्लिक करें
- GitHub पर बैकअप लेने के लिए **Push origin** पर क्लिक करें
- दोहराएं

---

निर्माता [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/), 7 दिसंबर, 2025।
