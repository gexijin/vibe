---
title: "Mac पर Claude Code इंस्टॉल करें"
lang: "hi"
---
[होम](./)

# Mac पर Claude Code इंस्टॉल करें

Claude Code एक AI सहायक है जो आपके Terminal में रहता है और आपको कोड लिखने, डीबग करने और समझने में मदद करता है। इसे एक जानकार कोडिंग पार्टनर की तरह सोचें जो जब भी आपको मदद चाहिए, उपलब्ध हो। चाहे आप बिल्कुल शुरुआती हों या अनुभवी डेवलपर, Claude Code आपके काम को तेज़ कर सकता है और आपको सीखने में मदद कर सकता है।

यह गाइड आपको इंस्टॉलेशन के हर चरण से, शुरुआती लोगों के लिए विस्तृत निर्देशों के साथ, गुज़ारेगी।

## अवलोकन

- Terminal खोलें
- Claude Code इंस्टॉल करें
- अपना API कनेक्शन कॉन्फ़िगर करें
- Claude Code का उपयोग शुरू करें

## मुख्य अवधारणाएँ

- **Terminal**: एक बिल्ट-इन Mac ऐप जहाँ आप बटन क्लिक करने के बजाय कमांड टाइप करते हैं। यही वह तरीका है जिससे आप Claude Code के साथ बातचीत करेंगे।
- **Claude Code**: एक AI कोडिंग सहायक जिसे आप Terminal में चलाते हैं। यह सवालों के जवाब दे सकता है, कोड लिख सकता है, और आपको मौजूदा प्रोजेक्ट समझने में मदद कर सकता है।

## आपको क्या चाहिए

- एक Mac कंप्यूटर (macOS 13.0 Ventura या नया)
- इंटरनेट कनेक्शन
- अपने कंप्यूटर पर एडमिनिस्ट्रेटर एक्सेस
- Claude Pro/Max सब्सक्रिप्शन या API कुंजी
- 5 - 10 मिनट

## चरण 1: Terminal खोलें

- अपने Dock में **Launchpad** आइकन पर क्लिक करें (रंगीन वर्गों वाला आइकन)
- ऊपर दिए गए सर्च बॉक्स में `Terminal` टाइप करें
- **Terminal** पर क्लिक करें (एक काला वर्गाकार आइकन)
- एक ब्लिंक करते कर्सर के साथ Terminal विंडो खुल जाएगी

**सुझाव:** अगले चरणों के लिए Terminal को खुला रखें।

## चरण 2: Claude Code इंस्टॉल करें

Terminal में, इस कमांड को कॉपी-पेस्ट करें, फिर **Return** दबाएँ:
```
curl -fsSL https://claude.ai/install.sh | bash
```

- Claude Code के इंस्टॉल होने की प्रतीक्षा करें (1-2 मिनट)
- आपको कुछ प्रोग्रेस मैसेज दिख सकते हैं - यह सामान्य है
- इंस्टॉलेशन पूरा होने पर, Terminal बंद करके फिर से खोलें, फिर इसे टाइप करके जाँचें:
   ```
   claude --version
   ```
- आपको Claude Code का वर्शन नंबर दिखना चाहिए

**विकल्प: Homebrew से इंस्टॉल करें**

यदि आप Homebrew का उपयोग करते हैं, तो आप Claude Code को इससे इंस्टॉल कर सकते हैं:
```
brew install --cask claude-code
```

**सुझाव:** यह जाँचने के लिए कि सब कुछ सही ढंग से सेट है, इंस्टॉलेशन के बाद `claude doctor` चलाएँ।

## चरण 3: अपने Anthropic खाते से कनेक्ट करें

### विकल्प A. अपने Claude Pro या Max सब्सक्रिप्शन का उपयोग करें

- Terminal में, टाइप करें:
   ```
   claude
   ```
- Claude एक ब्राउज़र खोलने की कोशिश करता है। यदि यह अपने आप नहीं खुलता, तो Terminal में दिखाए गए URL को कॉपी करके अपने ब्राउज़र में पेस्ट करें।
- अपने Claude.ai खाते में लॉगिन करें (यह अपने आप भी हो सकता है)
- **Authorize** पर क्लिक करें
- जब एक लंबा कोड दिखाई दे तो **Copy Code** पर क्लिक करें
- वापस Terminal विंडो पर जाएँ
- Terminal में पेस्ट करने के लिए: मेनू बार में **Edit** पर क्लिक करें, फिर **Paste** पर क्लिक करें
- आपको एक सफलता संदेश दिखना चाहिए
- सेटअप पूरा करने के लिए निर्देशों का पालन करें

### विकल्प B. Anthropic API कुंजी का उपयोग करें

यदि आपके पास Claude सब्सक्रिप्शन के बजाय Anthropic API कुंजी है:

- सबसे पहले, [Anthropic Console](https://console.anthropic.com/) से अपनी API कुंजी प्राप्त करें
- Terminal में, टाइप करें:
   ```
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   `your-api-key-here` को अपनी वास्तविक API कुंजी से बदलें
- इसे स्थायी बनाने के लिए (ताकि आपको इसे हर बार सेट न करना पड़े), इसे अपनी शेल प्रोफाइल में जोड़ें:
   ```
   echo 'export ANTHROPIC_API_KEY="your-api-key-here"' >> ~/.zshrc
   ```
   `your-api-key-here` को अपनी वास्तविक API कुंजी से बदलें
- बदलाव लागू होने के लिए Terminal बंद करके फिर से खोलें

**नोट:** यदि आप zsh के बजाय bash वाले पुराने Mac का उपयोग कर रहे हैं, तो ऊपर दिए गए कमांड में `~/.zshrc` की जगह `~/.bash_profile` लिखें।

### विकल्प C. OpenRouter API का उपयोग करें (मुफ़्त शुरुआत!)

OpenRouter एक यूनिफाइड API गेटवे है जो एक ही API कुंजी के ज़रिए 500+ बड़े लैंग्वेज मॉडलों तक पहुँच प्रदान करता है। यह Claude Code का उपयोग करने का एक किफ़ायती तरीका हो सकता है, क्योंकि आप केवल उपयोग के लिए भुगतान करते हैं और विभिन्न कीमतों वाले मॉडलों में से चुन सकते हैं।

- [openrouter.ai](https://openrouter.ai) पर साइन अप करें और लॉगिन करें
- **Get API key** पर क्लिक करें और कुंजी को किसी सुरक्षित जगह कॉपी करें
- Claude Code शुरू करने से पहले आवश्यक एनवायरनमेंट वेरिएबल सेट करें:
   ```
   export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
   export ANTHROPIC_AUTH_TOKEN="your-openrouter-api-key"
   export ANTHROPIC_API_KEY=""
   export ANTHROPIC_DEFAULT_SONNET_MODEL="openai/gpt-5.1-codex-max"
   export ANTHROPIC_DEFAULT_OPUS_MODEL="openai/gpt-5.2-pro"
   export ANTHROPIC_DEFAULT_HAIKU_MODEL="minimax/minimax-m2:exacto"
   ```
- Claude Code शुरू करें:
   ```
   claude
   ```
- Claude Code में `/status` टाइप करके कनेक्शन जाँचें

**नोट्स:**
- `your-openrouter-api-key` को अपनी वास्तविक OpenRouter API कुंजी से बदलें
- `ANTHROPIC_API_KEY` को स्पष्ट रूप से खाली सेट किया जाना चाहिए
- वैकल्पिक मॉडलों का उपयोग करने के लिए, उनमें **टूल यूज़ क्षमताएँ** होनी चाहिए। आप मॉडल इस तरह ओवरराइड कर सकते हैं:
   ```
   export ANTHROPIC_DEFAULT_SONNET_MODEL="model-provider/model-name"
   ```
- उपलब्ध मॉडल [openrouter.ai/models](https://openrouter.ai/models) पर ब्राउज़ करें
- फ्री टियर आपको प्रतिदिन 50 API रिक्वेस्ट देता है
- अधिक जानकारी के लिए [आधिकारिक OpenRouter गाइड](https://openrouter.ai/docs/guides/claude-code-integration) देखें


### विकल्प D. Azure Foundry के ज़रिए Anthropic API का उपयोग करें

यह विकल्प उन संगठनों के लिए है जो Azure-होस्टेड Claude मॉडलों का उपयोग करते हैं। Terminal विंडो में, एनवायरनमेंट वेरिएबल परिभाषित करने के लिए यह कोड पेस्ट करें (Claude शुरू करने से पहले):
```
# Microsoft Foundry इंटीग्रेशन सक्षम करें
export CLAUDE_CODE_USE_FOUNDRY=1
# Azure रिसोर्स का नाम
export ANTHROPIC_FOUNDRY_RESOURCE=xxxx-eastus2
# अपने रिसोर्स के डिप्लॉयमेंट नामों पर मॉडल सेट करें
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-5
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-5
export ANTHROPIC_FOUNDRY_API_KEY=your_api_key
```

**नोट:** `xxxx-eastus2` को अपने Foundry Resource के नाम से बदलें (पूरा बेस URL इस्तेमाल न करें)। `your_api_key` को अपने Azure पोर्टल की पूरी API कुंजी से बदलें।

## चरण 4: Claude Code का परीक्षण करें

अब आप तैयार हैं! Claude Code का उपयोग करने का तरीका यहाँ है:

- Terminal में, टाइप करें:
   ```
   claude
   ```
- बातचीत के लिए तैयार होने से पहले यह आपसे कुछ सवाल पूछता है
- यह जाँचने के लिए कि यह काम कर रहा है, कोई सामान्य सवाल पूछें, जैसे "Explain quantum computing."

## चरण 5: अपने प्रोजेक्ट पर जाएँ

- यदि आपके Mac फ़ोल्डरों में कोई प्रोजेक्ट है, तो आप उस पर जा सकते हैं:
   ```
   cd ~/Documents/test_claude
   ```
   `test_claude` को अपने असली प्रोजेक्ट फ़ोल्डर के नाम से बदलें

- फिर Claude शुरू करें:
   ```
   claude
   ```
- Claude से कोडबेस को आपको समझाने के लिए कहकर शुरुआत करें।
- आप Claude से बदलाव करने के लिए कह सकते हैं।
- अपने पसंदीदा IDE में अपने कोड का परीक्षण करें।

**नोट:** Claude एक प्रोजेक्ट फ़ोल्डर के भीतर काम करता है। यह उस फ़ोल्डर में लिखने की अनुमतियाँ तय करता है और सेटिंग्स उसी फ़ोल्डर में सेव करता है। यह Claude का वर्कस्पेस है।

## चरण 6: Claude Code अपडेट करें

नेटिव इंस्टॉलर से इंस्टॉल किया गया Claude Code बैकग्राउंड में अपने आप अपडेट हो जाता है। आप मैन्युअल रूप से भी अपडेट शुरू कर सकते हैं:

- Terminal में, टाइप करें:
   ```
   sudo claude
   ```
- Claude Code अपडेट्स की जाँच करेगा और नवीनतम वर्शन इंस्टॉल करेगा

**नोट:** Homebrew इंस्टॉलेशन अपने आप अपडेट नहीं होते। नवीनतम वर्शन पाने के लिए समय-समय पर `brew upgrade claude-code` चलाएँ।

## अगले कदम
- [VS Code Getting Started](./VS_Code_Getting_Started.md) - एक लोकप्रिय कोड एडिटर, VS Code का उपयोग करना सीखें
- [Claude Code in VS Code (Mac)](./Claude_Code_in_VS_Code_Mac.md) - VS Code के भीतर Claude Code चलाएँ
- [Writing a Research Paper with Claude Code](./Writing_Research_Paper_Claude_Code.md) - अकादमिक लेखन के लिए Claude Code का उपयोग करें

## Terminal को फिर से कैसे खोलें

Terminal बंद करने के बाद, इसे फिर से खोलने का तरीका यहाँ है:

- अपने Dock में **Launchpad** आइकन पर क्लिक करें (रंगीन वर्गों वाला आइकन)
- ऊपर दिए गए सर्च बॉक्स में `Terminal` टाइप करें
- **Terminal** पर क्लिक करें
- एक Terminal विंडो खुल जाएगी

## समस्या निवारण

### पहला चरण: Claude Doctor चलाएँ
यदि कुछ काम नहीं कर रहा है, तो पहले यह कमांड चलाएँ:
```
claude doctor
```
यह आपके इंस्टॉलेशन की जाँच करता है और किसी भी समस्या की रिपोर्ट करता है।

### इंस्टॉलेशन स्क्रिप्ट विफल होती है
- सुनिश्चित करें कि आपके पास macOS 13.0 या नया वर्शन है
- Homebrew विकल्प आज़माएँ: `brew install --cask claude-code`
- अपना इंटरनेट कनेक्शन जाँचें और फिर से कोशिश करें

### Claude Code कमांड नहीं मिलता
- Terminal को पूरी तरह बंद करें (मेनू बार में **Terminal** पर क्लिक करें, फिर **Quit Terminal**)
- Terminal फिर से खोलें
- यह जाँचने के लिए `claude --version` आज़माएँ कि यह इंस्टॉल है या नहीं
- इंस्टॉलेशन कमांड फिर से चलाने की कोशिश करें: `curl -fsSL https://claude.ai/install.sh | bash`

### प्रमाणीकरण विफल होता है
- सुनिश्चित करें कि आपके पास सक्रिय Claude Pro/Max सब्सक्रिप्शन या वैध API कुंजी है
- `claude` को फिर से चलाने की कोशिश करें और लॉगिन प्रक्रिया पूरी करें
- जाँचें कि आपके ब्राउज़र ने सही ऑथराइज़ेशन पेज खोला है

## Mac उपयोगकर्ताओं के लिए सुझाव

### प्रोजेक्ट पाथ खोजना
किसी फ़ोल्डर का पाथ खोजने के लिए:
- Finder खोलें
- अपने प्रोजेक्ट फ़ोल्डर पर जाएँ
- फ़ोल्डर को खींचकर Terminal में छोड़ें - पूरा पाथ दिख जाएगा!

### अलग-अलग Terminal ऐप्स का उपयोग करना
आप इन जैसे अन्य टर्मिनल ऐप्स का भी उपयोग कर सकते हैं:
- iTerm2 (अधिक सुविधाओं वाला लोकप्रिय विकल्प)
- Warp (AI सुविधाओं वाला आधुनिक टर्मिनल)
- Hyper (क्रॉस-प्लेटफ़ॉर्म टर्मिनल)

Claude Code इन सभी के साथ काम करता है!

## मदद चाहिए?

- Claude Code से जुड़ी समस्याओं के लिए: [Claude Code GitHub](https://github.com/anthropics/claude-code)
- आधिकारिक सेटअप दस्तावेज़ों के लिए: [Claude Code Setup Guide](https://code.claude.com/docs/en/setup)

---

*अंतिम अपडेट: फ़रवरी 2026*
