---
title: "Windows पर Claude Code इंस्टॉल करें"
lang: "hi"
---
[होम](./)

# Windows पर Claude Code इंस्टॉल करें

Claude Code एक AI सहायक है जो आपके terminal में रहता है और आपको कोड लिखने, डीबग करने और समझने में मदद करता है। यह गाइड आपको बस कुछ ही मिनटों में Windows पर सीधे चलाने के लिए तैयार करता है। अंत में एक वैकल्पिक, अधिक उन्नत सेटअप के रूप में WSL2 भी उपलब्ध है।

## मुख्य अवधारणाएँ

- **PowerShell** - Windows का बिल्ट-इन कमांड-लाइन टूल, जिसका उपयोग यहाँ Claude Code इंस्टॉल करने और चलाने के लिए किया जाता है
- **Git for Windows** - एक मुफ़्त डाउनलोड जो **Git Bash** जोड़ता है, वह शेल जिसका उपयोग Claude Code कमांड चलाने के लिए करता है
- **WSL (Windows Subsystem for Linux)** - एक वैकल्पिक Windows फ़ीचर जो Windows के साथ-साथ एक वास्तविक Linux सिस्टम चलाता है, जिसका उपयोग अंत में उन्नत सेटअप के लिए किया जाता है

## आपको क्या चाहिए

- एक Windows 10 या Windows 11 कंप्यूटर
- Claude Pro/Max सब्सक्रिप्शन, या एक API कुंजी
- 5 - 10 मिनट

## चरण 1: Git for Windows इंस्टॉल करें (वैकल्पिक, अनुशंसित)

Git for Windows **अनुशंसित है लेकिन वैकल्पिक**। यह **Git Bash** जोड़ता है, वह शेल जिसका उपयोग Claude Code कमांड चलाने के लिए करता है। यदि आप इस चरण को छोड़ देते हैं, तो Claude Code इसके बजाय PowerShell का उपयोग करने लगता है - इसलिए यदि आप चाहें तो सीधे चरण 2 पर जा सकते हैं और बाद में Git इंस्टॉल कर सकते हैं।

- [git-scm.com/download/win](https://git-scm.com/download/win) पर जाएँ
- डाउनलोड अपने आप शुरू हो जाना चाहिए - खत्म होने पर इंस्टॉलर खोलें
- डिफ़ॉल्ट विकल्पों को स्वीकार करते हुए इंस्टॉलर में **Next** पर क्लिक करते जाएँ
- **Install** पर क्लिक करें, फिर **Finish**

बस इतना ही - Claude Code शुरू होने पर Git Bash को अपने आप पहचान लेगा।

## चरण 2: Claude Code इंस्टॉल करें

- **Windows Start बटन** पर क्लिक करें
- `PowerShell` टाइप करें और **Windows PowerShell** पर क्लिक करें
- PowerShell विंडो में, टाइप करें:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- इंस्टॉलेशन पूरा होने की प्रतीक्षा करें
- PowerShell बंद करके फिर से खोलें, फिर इसे टाइप करके जाँचें:
   ```
   claude --version
   ```
- आपको Claude Code का वर्शन नंबर दिखना चाहिए

## चरण 3: VS Code में Claude Code खोलें

अब जब Claude Code इंस्टॉल हो चुका है, आप इसे केवल terminal में ही नहीं, बल्कि VS Code के भीतर भी उपयोग कर सकते हैं। यह अक्सर काम करने का सबसे आसान तरीका है क्योंकि आप अपने एडिटर को छोड़े बिना फ़ाइलें पढ़ सकते हैं, कोड एडिट कर सकते हैं, और मदद माँग सकते हैं।

Claude Code साइडबार को VS Code के भीतर एक चैट विंडो की तरह समझें। यह आपको सवाल पूछने, कोड समझाने और एक ही स्क्रीन पर काम करते हुए मदद पाने देता है।

### Claude Code साइडबार कैसे खोलें

1. VS Code खोलें
2. विंडो के बिल्कुल बाईं ओर देखें
3. यदि आपको Claude Code पैनल पहले से नहीं दिखता, तो Extensions आइकन पर क्लिक करें
4. Extensions मार्केटप्लेस में Claude Code खोजें
5. यदि पहले से इंस्टॉल नहीं है तो Install पर क्लिक करें
6. इंस्टॉलेशन के बाद, बाएँ साइडबार में Claude Code आइकन देखें

यदि आपको Claude Code आइकन नहीं दिखता, तो यह आज़माएँ:

1. Ctrl + Shift + P दबाएँ
2. टाइप करें: Claude Code: Open Sidebar
3. सूची में मिलते-जुलते विकल्प पर क्लिक करें

यदि तब भी नहीं दिखता, तो VS Code बंद करके फिर से खोलें। कभी-कभी एक्सटेंशन को साइडबार दिखने से पहले एक नई शुरुआत की ज़रूरत होती है।

### साइडबार किस काम आता है

Claude Code साइडबार वह जगह है जहाँ आप ये कर सकते हैं:

- अपने प्रोजेक्ट के बारे में सवाल पूछें
- त्रुटियाँ ठीक करने में मदद पाएँ
- वह कोड समझें जो आपको समझ नहीं आता
- फ़ाइलें बनाएँ या अपडेट करें
- VS Code के भीतर रहते हुए ज़्यादा विज़ुअल तरीके से काम करें

यह इसलिए उपयोगी है क्योंकि आप अपना कोड एडिटर में खुला रख सकते हैं और उसी विंडो में Claude से मदद माँग सकते हैं।

### त्वरित परीक्षण

साइडबार खुलने के बाद:

- टाइप करें: Explain this project to me
- Enter दबाएँ

यदि Claude जवाब देता है, तो आप इसका उपयोग करने के लिए तैयार हैं।

> सुझाव: यदि साइडबार अभी भी नहीं दिखता, तो सुनिश्चित करें कि Claude Code एक्सटेंशन इंस्टॉल है और VS Code को रीस्टार्ट किया गया है।

## चरण 4: अपने Anthropic खाते से कनेक्ट करें

### विकल्प A. अपने Claude Pro या Max सब्सक्रिप्शन का उपयोग करें

- PowerShell विंडो में, टाइप करें:
   ```
   claude
   ```
- Claude एक ब्राउज़र खोलने की कोशिश करता है। यदि यह अपने आप नहीं खुल पाता, तो **Ctrl** दबाए रखकर लंबे URL पर क्लिक करें ताकि वह ब्राउज़र में खुले। वैकल्पिक रूप से, URL कॉपी करके किसी बाहरी ब्राउज़र में पेस्ट करें।
- अपने Claude.ai खाते में लॉगिन करें (यदि आप Chrome उपयोग कर रहे हैं तो यह अपने आप हो सकता है)
- **Authorize** पर क्लिक करें
- जब एक लंबा कोड दिखाई दे तो **Copy Code** पर क्लिक करें
- वापस terminal विंडो पर जाएँ
- terminal में पेस्ट करने के लिए: **राइट-क्लिक** करें और **Paste** चुनें (या **Ctrl+Shift+V** दबाएँ)
- आपको एक सफलता संदेश दिखना चाहिए
- सेटअप पूरा करने के लिए निर्देशों का पालन करें

नीचे दिए गए API-आधारित विकल्प **PowerShell** में ही रहते हैं और `setx` कमांड का उपयोग करते हैं, जो किसी सेटिंग को स्थायी रूप से सेव करता है। `setx` चलाने के बाद, बदलाव लागू होने के लिए **PowerShell बंद करके फिर से खोलें**, फिर `claude` शुरू करें।

### विकल्प B. Anthropic API कुंजी का उपयोग करें

यदि आपके पास Claude सब्सक्रिप्शन के बजाय Anthropic API कुंजी है:

- [Anthropic Console](https://console.anthropic.com/) से अपनी API कुंजी प्राप्त करें
- PowerShell में, टाइप करें:
   ```
   setx ANTHROPIC_API_KEY "your-api-key-here"
   ```
   `your-api-key-here` को अपनी वास्तविक API कुंजी से बदलें
- बदलाव लागू होने के लिए PowerShell बंद करके फिर से खोलें
- Claude Code शुरू करें:
   ```
   claude
   ```

### विकल्प C. OpenRouter API का उपयोग करें (मुफ़्त शुरुआत!)

OpenRouter एक यूनिफाइड API गेटवे है जो एक ही API कुंजी के ज़रिए 500+ बड़े लैंग्वेज मॉडलों तक पहुँच प्रदान करता है। यह Claude Code का उपयोग करने का एक किफ़ायती तरीका हो सकता है, क्योंकि आप केवल उपयोग के लिए भुगतान करते हैं और विभिन्न कीमतों वाले मॉडलों में से चुन सकते हैं।

- [openrouter.ai](https://openrouter.ai) पर साइन अप करें और लॉगिन करें
- **Get API key** पर क्लिक करें और कुंजी को किसी सुरक्षित जगह कॉपी करें
- PowerShell में, आवश्यक एनवायरनमेंट वेरिएबल सेट करें:
   ```
   setx ANTHROPIC_BASE_URL "https://openrouter.ai/api"
   setx ANTHROPIC_AUTH_TOKEN "your-openrouter-api-key"
   setx ANTHROPIC_API_KEY ""
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "openai/gpt-5.1-codex-max"
   setx ANTHROPIC_DEFAULT_OPUS_MODEL "openai/gpt-5.2-pro"
   setx ANTHROPIC_DEFAULT_HAIKU_MODEL "minimax/minimax-m2:exacto"
   ```
- PowerShell बंद करके फिर से खोलें, फिर Claude Code शुरू करें:
   ```
   claude
   ```
- Claude Code में `/status` टाइप करके कनेक्शन जाँचें

**नोट्स:**
- `your-openrouter-api-key` को अपनी वास्तविक OpenRouter API कुंजी से बदलें
- `ANTHROPIC_API_KEY` को स्पष्ट रूप से खाली सेट किया जाना चाहिए
- वैकल्पिक मॉडलों का उपयोग करने के लिए, उनमें **टूल यूज़ क्षमताएँ** होनी चाहिए। आप मॉडल इस तरह ओवरराइड कर सकते हैं:
   ```
   setx ANTHROPIC_DEFAULT_SONNET_MODEL "model-provider/model-name"
   ```
- उपलब्ध मॉडल [openrouter.ai/models](https://openrouter.ai/models) पर ब्राउज़ करें
- फ्री टियर आपको प्रतिदिन 50 API रिक्वेस्ट देता है
- अधिक जानकारी के लिए [आधिकारिक OpenRouter गाइड](https://openrouter.ai/docs/guides/claude-code-integration) देखें

### विकल्प D. Azure Foundry के ज़रिए Anthropic API का उपयोग करें

PowerShell में, एनवायरनमेंट वेरिएबल परिभाषित करने के लिए यह कोड पेस्ट करें:
```
# Microsoft Foundry इंटीग्रेशन सक्षम करें
setx CLAUDE_CODE_USE_FOUNDRY 1
# Azure रिसोर्स का नाम
setx ANTHROPIC_FOUNDRY_RESOURCE "xxxx-eastus2"
# अपने रिसोर्स के डिप्लॉयमेंट नामों पर मॉडल सेट करें
setx ANTHROPIC_DEFAULT_OPUS_MODEL "claude-opus-4-5"
setx ANTHROPIC_DEFAULT_SONNET_MODEL "claude-sonnet-4-5"
setx ANTHROPIC_DEFAULT_HAIKU_MODEL "claude-haiku-4-5"
setx ANTHROPIC_FOUNDRY_API_KEY "your_api_key"
```

**नोट:** `xxxx-eastus2` को अपने Foundry Resource के नाम से बदलें (पूरा बेस URL इस्तेमाल न करें)। `your_api_key` को अपने Azure पोर्टल की पूरी API कुंजी से बदलें।

फिर PowerShell बंद करके फिर से खोलें, और Claude Code शुरू करें:
```
claude
```

अब आप Azure पर डिप्लॉय किए गए Claude मॉडलों के साथ Claude Code का उपयोग कर पाएँगे।

## चरण 5: Claude Code का परीक्षण करें

अब आप तैयार हैं! PowerShell में `claude` टाइप करें और कोई सामान्य सवाल पूछें, जैसे "Explain quantum computing."

## चरण 6: अपने प्रोजेक्ट एक्सेस करें

- यदि आपके पास कोई प्रोजेक्ट फ़ोल्डर है, तो PowerShell में उस पर जाएँ:
   ```
   cd ~/Documents/test_claude
   ```
- फिर Claude शुरू करें:
   ```
   claude
   ```
- Claude से कोडबेस को आपको समझाने के लिए कहकर शुरुआत करें।
- आप Claude से बदलाव करने के लिए कह सकते हैं।
- अपने पसंदीदा IDE में अपने कोड का परीक्षण करें।

**नोट:** Claude एक प्रोजेक्ट फ़ोल्डर के भीतर काम करता है। यह उसी फ़ोल्डर में सेटिंग्स सेव करता है। यह Claude का वर्कस्पेस है।

## चरण 7: (वैकल्पिक) पूर्ण Linux अनुभव के लिए WSL2 इंस्टॉल करें

ऊपर बताया गया नेटिव सेटअप ज़्यादातर लोगों के लिए काफ़ी है। लेकिन Claude Code Linux पर बेहतर प्रदर्शन करता है। WSL2 Windows के भीतर एक वास्तविक Linux सिस्टम चलाता है और **Bash टूल सैंडबॉक्सिंग** (एक सुरक्षा फ़ीचर) के साथ-साथ Linux टूलचेन के साथ बेहतर संगतता जोड़ता है। इसे सेट करने में ज़्यादा समय लगता है और रीस्टार्ट की ज़रूरत पड़ती है, इसलिए यह तभी करें जब आप पूरा Linux अनुभव चाहते हों।

### a) वर्चुअलाइज़ेशन जाँचें और WSL इंस्टॉल करें

**पहले, जाँचें कि वर्चुअलाइज़ेशन सक्षम है या नहीं:**

- टास्कबार पर (आपकी स्क्रीन के नीचे की पट्टी) **राइट-क्लिक** करें
- मेनू से **Task Manager** पर क्लिक करें
- यदि Task Manager एक छोटी विंडो में खुलता है, तो नीचे **More details** पर क्लिक करें
- ऊपर **Performance** टैब पर क्लिक करें
- बाईं साइडबार में **CPU** पर क्लिक करें
- वह पंक्ति खोजें जिस पर **Virtualization:** लिखा है और देखें कि क्या इस पर **Enabled** लिखा है

**यदि इस पर "Disabled" लिखा है:** आपको अपने कंप्यूटर की BIOS सेटिंग्स में वर्चुअलाइज़ेशन सक्षम करना होगा:
- अपना कंप्यूटर रीस्टार्ट करें
- स्टार्टअप के दौरान, BIOS की (आमतौर पर **F2**, **F10**, **Del**, या **Esc** - यह आपके कंप्यूटर निर्माता पर निर्भर करता है) दबाएँ
- "Virtualization Technology", "Intel VT-x", "AMD-V", या "SVM Mode" से संबंधित सेटिंग्स खोजें
- इन सेटिंग्स को सक्षम करें
- BIOS सेव करके बाहर निकलें (आमतौर पर **F10**)

**अब WSL इंस्टॉल करें:**

- **Windows Start बटन** पर क्लिक करें, `PowerShell` टाइप करें
- **Windows PowerShell** पर **राइट-क्लिक** करें और **Run as administrator** पर क्लिक करें
- "क्या आप इस ऐप को अपने डिवाइस में बदलाव करने की अनुमति देना चाहते हैं?" पूछे जाने पर **Yes** पर क्लिक करें
- PowerShell विंडो में, टाइप करें:
   ```
   wsl --install
   ```
- आपको "Installing: Windows Subsystem for Linux" और "Installing: Ubuntu" जैसे संदेश दिख सकते हैं
- इंस्टॉलेशन पूरा होने पर, अपना कंप्यूटर रीस्टार्ट करें

**नोट:** `wsl --install` के लिए Windows 10 वर्शन 2004 या उससे ऊपर, या Windows 11 चाहिए। यदि कमांड पहचाना नहीं जाता, तो हो सकता है आपका Windows वर्शन बहुत पुराना हो।

### b) Ubuntu सेट अप करें

आपके कंप्यूटर के रीस्टार्ट होने के बाद, "Ubuntu" शीर्षक वाली एक terminal विंडो 2-5 मिनट में अपने आप खुल जानी चाहिए। यदि ऐसा नहीं होता, तो **Windows Start बटन** पर क्लिक करें, `Ubuntu` टाइप करें, और **Ubuntu** ऐप (नारंगी गोल आइकन) पर क्लिक करें।

- इस संदेश की प्रतीक्षा करें: `Enter new UNIX username:`
- एक यूज़रनेम टाइप करें (केवल छोटे अक्षर और नंबर, कोई स्पेस नहीं) - उदाहरण के लिए `john`
- आपको दिखेगा: `New password:`
- एक आसान पासवर्ड टाइप करें (टाइप करते समय अक्षर नहीं दिखेंगे - यह सामान्य है)
- पूछे जाने पर वही पासवर्ड फिर से टाइप करें

**महत्वपूर्ण:** इस यूज़रनेम और पासवर्ड को याद रखें - बाद में आपको इनकी ज़रूरत पड़ेगी।

### c) WSL में Claude Code इंस्टॉल करें

- Ubuntu terminal में, टाइप करें:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
- यह टाइप करके जाँचें:
   ```
   claude --version
   ```
- Ubuntu terminal में `claude` टाइप करके और ब्राउज़र लॉगिन का पालन करके अपना खाता कनेक्ट करें (यह चरण 3, विकल्प A जैसा ही है)। यदि आप इसके बजाय API कुंजी उपयोग करते हैं, तो इसे `export ANTHROPIC_API_KEY="your-api-key-here"` से सेट करें (WSL Linux कमांड इस्तेमाल करता है, `setx` नहीं)
- WSL से किसी Windows प्रोजेक्ट फ़ोल्डर को खोलने के लिए:
   ```
   cd /mnt/c/Users/Username/Documents/test_claude
   ```
   `Username` को अपने असली Windows यूज़रनेम से बदलें।

## अगले कदम

- **VS Code सेट अप करें**: [VS Code Getting Started](VS_Code_Getting_Started) गाइड का पालन करें, फिर इसे [Claude Code in VS Code (Windows)](Claude_Code_in_VS_Code_Win) से Claude Code से जोड़ें
- **Git की मूल बातें सीखें**: [Claude Code Git on Windows](Claude_Code_Git_Windows) से अपने प्रोजेक्ट में वर्शन कंट्रोल जोड़ें
- **एक प्रोजेक्ट आज़माएँ**: क्रिया में Claude Code देखने के लिए [Writing a Research Paper with Claude Code](Writing_Research_Paper_Claude_Code) पर काम करें

## समस्या निवारण

### पहला चरण: Claude Doctor चलाएँ

यदि कुछ काम नहीं कर रहा है, तो पहले यह कमांड चलाने की कोशिश करें:
```
claude doctor
```
यह बिल्ट-इन डायग्नोस्टिक टूल आपके इंस्टॉलेशन की जाँच करता है और सामान्य समस्याओं की रिपोर्ट करता है।

### Claude कमांड नहीं मिलता (नेटिव Windows)

- PowerShell बंद करके फिर से खोलें
- इंस्टॉलेशन कमांड फिर से चलाने की कोशिश करें:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
- सुनिश्चित करें कि आपके PATH में Claude इंस्टॉलेशन डायरेक्टरी शामिल है

### "Please enable the Virtual Machine Platform Windows feature and ensure virtualization is enabled in the BIOS"
इस त्रुटि का मतलब है कि वर्चुअलाइज़ेशन सक्षम नहीं है:
- यह देखने के लिए Task Manager जाँचें कि वर्चुअलाइज़ेशन सक्षम है या नहीं (ऊपर दिया गया वैकल्पिक WSL सेक्शन देखें)
- यदि अक्षम है, तो इसे अपने कंप्यूटर के BIOS में सक्षम करें
- वर्चुअलाइज़ेशन सक्षम करने के बाद, कंप्यूटर रीस्टार्ट करें और फिर से `wsl --install` आज़माएँ

### "wsl --install" काम नहीं करता
- सुनिश्चित करें कि आप PowerShell को Administrator के रूप में चला रहे हैं
- सुनिश्चित करें कि आपके पास Windows 10 वर्शन 2004+ या Windows 11 है
- पहले `wsl --update` चलाने की कोशिश करें, फिर फिर से `wsl --install` आज़माएँ

### रीस्टार्ट के बाद Ubuntu विंडो नहीं खुलती
- **Windows Start बटन** पर क्लिक करें, `Ubuntu` टाइप करें, और इसे मैन्युअल रूप से चलाने के लिए **Ubuntu** ऐप पर क्लिक करें

## मदद चाहिए?

- WSL समस्याओं के लिए: [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- Claude Code से जुड़ी समस्याओं के लिए: [Claude Code GitHub](https://github.com/anthropics/claude-code)

---

निर्माता: [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/), 11 दिसंबर, 2025। अद्यतन: जून 2026।
