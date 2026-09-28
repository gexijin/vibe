---
title: "Docker Container के ज़रिए VS Code में Python कोडिंग"
lang: "hi"
---
[होम](./)

# Docker Container के ज़रिए VS Code में Python कोडिंग

कभी अपना Python कोड किसी सहकर्मी के साथ साझा करने की कोशिश की और "लेकिन यह मेरी मशीन पर तो काम करता है" जैसी समस्याओं को सुलझाने में घंटों बिताए? Docker container कोड के लिए शिपिंग कंटेनर जैसे हैं—वे आपके Python एनवायरनमेंट, लाइब्रेरी, और डिपेंडेंसी को एक सील किए हुए बॉक्स में पैक कर देते हैं जो हर जगह एक जैसा काम करता है। इसके अलावा, आपको [Docker Hub](https://hub.docker.com/) पर हज़ारों पहले से बने इमेज तक पहुँच मिलती है, जहाँ सॉफ़्टवेयर डेवलपर तैयार-उपयोग एनवायरनमेंट पब्लिश करते हैं, जिससे मैन्युअल सॉफ़्टवेयर इंस्टॉलेशन की परेशानी नहीं होती। यह ट्यूटोरियल आपको दिखाता है कि VS Code और Docker Desktop का उपयोग करके एक अलग, दोहराने योग्य (reproducible) एनवायरनमेंट में Python कैसे चलाएँ।

## मुख्य अवधारणाएँ

- **[Docker Desktop](https://www.docker.com/products/docker-desktop/)** - आपके कंप्यूटर पर container चलाने वाला ऐप्लिकेशन, जो अलग-अलग एनवायरनमेंट का प्रबंधन करता है
- **[Dev Container](https://code.visualstudio.com/docs/devcontainers/containers)** - VS Code का एक फ़ीचर जो आपको पूरे IDE सपोर्ट के साथ Docker container के भीतर कोड करने देता है
- **Container Isolation** - आपका कोड एक अलग Linux एनवायरनमेंट में चलता है जो केवल आपका प्रोजेक्ट फ़ोल्डर देखता है, आपका पूरा कंप्यूटर नहीं
- **[Python Official Images](https://hub.docker.com/_/python)** - Python और ज़रूरी टूल पहले से इंस्टॉल किए हुए पहले से बने Docker इमेज

## आपको क्या चाहिए

- पूरा किया हुआ [Python Coding in VS Code](./Python_Coding_VS_Code_Guide)
- 20-25 मिनट

## चरण 1: Docker Desktop इंस्टॉल करें

- [Docker Desktop डाउनलोड पेज](https://www.docker.com/products/docker-desktop/) पर जाएँ
- अपने सिस्टम के अनुसार **Download for Windows** (या Mac/Linux) पर क्लिक करें
- इंस्टॉलर चलाएँ और इंस्टॉलेशन विज़ार्ड का पालन करें
- पूछे जाने पर, WSL 2 सक्षम करें (Windows उपयोगकर्ता) या डिफ़ॉल्ट सेटिंग्स स्वीकार करें
- इंस्टॉलेशन के बाद, Docker Desktop लॉन्च करें
- Docker इंजन के शुरू होने की प्रतीक्षा करें (आपको नीचे बाईं ओर एक हरे रंग का स्टेटस इंडिकेटर दिखेगा)

## चरण 2: Dev Containers Extension इंस्टॉल करें

- VS Code खोलें
- बाएँ साइडबार में **Extensions** आइकन पर क्लिक करें (या **View > Extensions** पर क्लिक करें)
- सर्च बॉक्स में `dev containers` टाइप करें
- Microsoft द्वारा बनाई गई **Dev Containers** खोजें
- **Install** पर क्लिक करें

## चरण 3: एक Python प्रोजेक्ट फ़ोल्डर बनाएँ

- अपने कंप्यूटर पर `python-docker-demo` नाम का एक नया फ़ोल्डर बनाएँ
- उसके अंदर, `.devcontainer` नाम का एक सबफ़ोल्डर बनाएँ
- उसके अंदर, `python` नाम का एक सबफ़ोल्डर बनाएँ
- आपकी संरचना ऐसी दिखनी चाहिए: `python-docker-demo/.devcontainer/` और `python-docker-demo/python/`

## चरण 4: Dockerfile बनाएँ

- VS Code में, **File > Open Folder** पर क्लिक करें
- अभी बनाए गए `python-docker-demo` फ़ोल्डर पर जाएँ
- **Select Folder** पर क्लिक करें
- Explorer साइडबार में, `.devcontainer` फ़ोल्डर पर राइट-क्लिक करें
- **New File** पर क्लिक करें
- इसे `Dockerfile` नाम दें
- नीचे दी गई सामग्री पेस्ट करें:

```dockerfile
# Choose the official Python slim image
FROM python:3.12-slim

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl build-essential && \
    rm -rf /var/lib/apt/lists/*

# 2. Install Python packages for data science and web apps
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter

# 3. Install Node.js LTS from NodeSource
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest

# 4. Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code

# 5. Expose Streamlit port
EXPOSE 8501
```

- **File > Save** पर क्लिक करें

## चरण 5: Dev Container कॉन्फ़िगरेशन बनाएँ

- `.devcontainer` फ़ोल्डर में, `devcontainer.json` नाम की एक नई फ़ाइल बनाएँ
- नीचे दी गई सामग्री पेस्ट करें:

```json
{
  "name": "Python in Docker",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.debugpy"
      ]
    }
  },
  "forwardPorts": [8501],
  "postCreateCommand": "python3 --version"
}
```

- **File > Save** पर क्लिक करें

## चरण 6: एक Python डेटा विश्लेषण स्क्रिप्ट बनाएँ

- `python` फ़ोल्डर में, `iris_analysis.py` नाम की एक नई फ़ाइल बनाएँ
- नीचे दी गई सामग्री पेस्ट करें:

```python
# Simple data analysis using the iris dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Display first few rows
print(df.head())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Create histograms
plt.figure(figsize=(10, 6))
plt.hist(df['sepal length (cm)'], bins=20, alpha=0.7, label='Sepal Length')
plt.hist(df['sepal width (cm)'], bins=20, alpha=0.7, label='Sepal Width')
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.title('Iris Sepal Measurements')
plt.legend()
plt.show()
```

- **File > Save** पर क्लिक करें

## चरण 7: एक Streamlit वेब ऐप बनाएँ

- `python` फ़ोल्डर में, `app.py` नाम की एक नई फ़ाइल बनाएँ
- नीचे दी गई सामग्री पेस्ट करें:

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Old Faithful Geyser Data")

# Slider for number of bins
bins = st.slider("Number of bins:", min_value=5, max_value=50, value=30)

# Generate sample data (simulating Old Faithful eruption durations)
np.random.seed(42)
data = np.concatenate([
    np.random.normal(2, 0.5, 100),
    np.random.normal(4.5, 0.5, 150)
])

# Create histogram
fig, ax = plt.subplots()
ax.hist(data, bins=bins, edgecolor='black')
ax.set_xlabel('Eruption Duration (minutes)')
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram with {bins} bins')

st.pyplot(fig)
```

- **File > Save** पर क्लिक करें

## चरण 8: Container में फिर से खोलें

- VS Code के नीचे-बाएँ कोने में हरे आइकन पर क्लिक करें
- मेनू से **Reopen in Container** चुनें
- VS Code container बनाएगा (पहली बार में इसमें 5-10 मिनट लगते हैं)
- आपको बिल्ड चरण दिखाने वाली एक प्रोग्रेस सूचना दिखेगी
- पूरा होने पर, हरा आइकन **Dev Container: Python in Docker** दिखाएगा

## चरण 9: Container एनवायरनमेंट को समझें

अब आप एक Linux container के भीतर कोडिंग कर रहे हैं। आइए समझें कि इसका क्या मतलब है।

- container के भीतर एक terminal खोलने के लिए **Terminal > New Terminal** पर क्लिक करें
- अपना वर्तमान स्थान जाँचें:

```bash
pwd
```

आपको `/workspaces/python-docker-demo` दिखेगा - यह container के भीतर आपका प्रोजेक्ट फ़ोल्डर है।

- फ़ाइलों की सूची देखें:

```bash
ls
```

आपको वे फ़ोल्डर दिखेंगे जो आपने बनाए थे: `.devcontainer/`, `python/`, आदि।

- एक डायरेक्टरी ऊपर जाने की कोशिश करें:

```bash
cd ..
ls
```

आपको केवल `python-docker-demo/` दिखेगा - container अलग-थलग (isolated) है। आप अपने कंप्यूटर के अन्य फ़ोल्डर, Desktop, या Documents तक नहीं पहुँच सकते। यह आइसोलेशन सुनिश्चित करता है कि आपका Python एनवायरनमेंट साफ़ और दोहराने योग्य (reproducible) है।

- प्रोजेक्ट फ़ोल्डर पर वापस जाएँ:

```bash
cd python-docker-demo
```

## चरण 10: Python कोड लाइन-दर-लाइन चलाएँ

Container में Python पहले से डेटा साइंस पैकेजों के साथ इंस्टॉल है। आइए विश्लेषण स्क्रिप्ट चलाएँ।

- VS Code Explorer में, `python/iris_analysis.py` पर जाएँ
- फ़ाइल खोलने के लिए क्लिक करें
- पहली लाइन चुनें: `import pandas as pd`
- इसे एक इंटरैक्टिव Python terminal में चलाने के लिए `Shift+Enter` दबाएँ
- नीचे एक Python terminal खुलता है
- `Shift+Enter` के साथ एक-एक करके हर लाइन या ब्लॉक चलाना जारी रखें
- जब आप `print(df.head())` चलाते हैं, तो आपको terminal में पहली 5 पंक्तियाँ दिखेंगी
- जब आप `print(df.describe())` चलाते हैं, तो आपको सांख्यिकीय सारांश दिखेंगे
- जब आप हिस्टोग्राम कोड चलाते हैं, तो विज़ुअलाइज़ेशन दिखाने वाली एक प्लॉट विंडो खुलेगी

## चरण 11: Streamlit ऐप चलाएँ

प्रोजेक्ट में एक डेमो Streamlit ऐप शामिल है जो एक इंटरैक्टिव हिस्टोग्राम बनाता है।

- VS Code Explorer में, `python/app.py` पर जाएँ
- फ़ाइल खोलने के लिए क्लिक करें
- एक नया terminal खोलें (**Terminal > New Terminal**)
- ऐप चलाएँ:

```bash
cd python
streamlit run app.py
```

- ऐप शुरू होगा और एक URL दिखाएगा: `http://localhost:8501`
- एक सूचना दिखेगी: **Open in Browser**
- **Open in Browser** पर क्लिक करें
- Streamlit ऐप आपके वेब ब्राउज़र में खुलता है
- हिस्टोग्राम बिन्स बदलने के लिए स्लाइडर को हिलाएँ - चार्ट रीयल-टाइम में अपडेट होता है

## चरण 12: एक साधारण बदलाव करें

आइए ऐप में बदलाव करें यह देखने के लिए कि डेवलपमेंट कैसे काम करता है।

- ऐप को चालू रखें
- VS Code में, `python/app.py` एडिट करें
- लाइन 6 खोजें: `st.title("Old Faithful Geyser Data")`
- इसे इस तरह बदलें:

```python
st.title("My First Python Docker App")
```

- **File > Save** पर क्लिक करें
- अपने ब्राउज़र पर वापस जाएँ
- ऊपर-दाएँ कोने में **Always rerun** पर क्लिक करें
- शीर्षक अब आपका कस्टम टेक्स्ट दिखाता है

## चरण 13: Dockerfile को समझना (वैकल्पिक)

- VS Code Explorer में, `.devcontainer/Dockerfile` पर जाएँ
- फ़ाइल खोलने के लिए क्लिक करें
- आपको पूरा कॉन्फ़िगरेशन दिखेगा

**मुख्य हिस्से:**

- `FROM python:3.12-slim` - आधिकारिक Python 3.12 बेस इमेज (हल्का, Debian-आधारित)
- `RUN apt-get install` - Python पैकेज बनाने के लिए Linux सिस्टम लाइब्रेरी
- `RUN pip install --no-cache-dir ...` - Python पैकेजों को स्थायी रूप से इंस्टॉल करता है
- `RUN curl... && apt-get install -y nodejs` - Node.js इंस्टॉल करता है, जो Claude Code चलाने के लिए ज़रूरी है
- `RUN npm install -g @anthropic-ai/claude-code` - AI सहायता के लिए Claude Code को ग्लोबली इंस्टॉल करता है
- `EXPOSE 8501` - Streamlit ऐप्स के लिए पोर्ट 8501 खोलता है

**अन्य Python इमेज जिनका आप उपयोग कर सकते हैं:**

- `python:3.12` - अधिक टूल के साथ पूरा Python इमेज (बड़ा आकार)
- `python:3.12-slim` - Python और pip वाला हल्का इमेज (जो हम उपयोग कर रहे हैं)
- `python:3.12-alpine` - न्यूनतम Alpine Linux-आधारित इमेज (सबसे छोटा आकार)
- `jupyter/datascience-notebook` - डेटा साइंस लाइब्रेरी के साथ पहले से कॉन्फ़िगर किया गया Jupyter

बेस इमेज बदलने के बाद, बदलाव लागू करने के लिए container को फिर से बिल्ड करें।

## चरण 14: Docker इमेज में Python पैकेज इंस्टॉल करें (वैकल्पिक)

terminal में pip से इंस्टॉल किए गए पैकेज (`pip install package`) अस्थायी होते हैं और container को फिर से बिल्ड करने पर गायब हो जाते हैं। पैकेजों को स्थायी बनाने के लिए, उन्हें Dockerfile में जोड़ें।

- VS Code Explorer में, `.devcontainer/Dockerfile` पर जाएँ
- फ़ाइल खोलने के लिए क्लिक करें
- लाइन 9 खोजें: `RUN pip install --no-cache-dir ...`
- सूची में `scikit-learn` जोड़ें:

```dockerfile
RUN pip install --no-cache-dir \
    pandas matplotlib seaborn streamlit jupyter scikit-learn
```

- **File > Save** पर क्लिक करें
- नीचे-बाएँ कोने में हरे आइकन पर क्लिक करें
- मेनू से **Rebuild Container** चुनें
- VS Code आपके नए पैकेज के साथ container को फिर से बिल्ड करेगा (इसमें 2-5 मिनट लगते हैं)
- सत्यापित करने के लिए, एक Python terminal खोलें और टाइप करें:

```python
import sklearn
print(sklearn.__version__)
```

यदि यह बिना किसी त्रुटि के वर्शन दिखाता है, तो पैकेज स्थायी रूप से इंस्टॉल हो गया है।

## अगले कदम

- **एक नई Python स्क्रिप्ट बनाएँ** - `python/` फ़ोल्डर में एक नई `.py` फ़ाइल बनाएँ, बिल्ट-इन डेटासेट का उपयोग करके या अपनी CSV फ़ाइलें लोड करके डेटा विश्लेषण कोड लिखें
- **Python पैकेज इंस्टॉल करें** - Dockerfile (लाइन 9) एडिट करके और container को फिर से बिल्ड करके ज़रूरी पैकेज जोड़ें
- **डेटा साइंस एक्सप्लोर करें** - pandas के साथ डेटा मैनिपुलेशन और matplotlib या seaborn के साथ विज़ुअलाइज़ेशन आज़माएँ
- **वेब ऐप बनाएँ** - Streamlit या Flask के साथ इंटरैक्टिव डैशबोर्ड बनाएँ

## समस्या निवारण

- **Docker Desktop नहीं चल रहा** - Docker Desktop खोलें और container फिर से खोलने से पहले हरे स्टेटस इंडिकेटर की प्रतीक्षा करें
- **Container बिल्ड विफल होता है** - अपना इंटरनेट कनेक्शन जाँचें; पहला बिल्ड इमेज और पैकेज डाउनलोड करता है। फिर से कोशिश करने के लिए **Rebuild Container** पर क्लिक करें
- **पोर्ट 8501 पहले से उपयोग में है** - उस पोर्ट का उपयोग करने वाले अन्य ऐप बंद करें, या Dockerfile और `devcontainer.json` में पोर्ट बदलें

## वर्कफ़्लो अवलोकन

यह सेटअप आपको एक पेशेवर Python डेवलपमेंट एनवायरनमेंट देता है:

- **VS Code** सिंटैक्स हाइलाइटिंग, IntelliSense, और डीबगिंग वाला कोड एडिटर प्रदान करता है
- **Docker container** Python और सभी डिपेंडेंसी के साथ एक अलग Linux एनवायरनमेंट चलाता है
- **Python official image** (`python:3.12-slim`) में Python, pip, और ज़रूरी टूल शामिल हैं
- **Dev Container config** (`.devcontainer/`) Python डीबगिंग और भाषा सपोर्ट के लिए VS Code एक्सटेंशन अपने आप इंस्टॉल करता है
- **Port forwarding** आपको अपने ब्राउज़र से container के भीतर चल रहे वेब ऐप (Streamlit, Flask) तक पहुँचने देता है

## रोज़मर्रा का वर्कफ़्लो

एक बार सब कुछ सेट हो जाने के बाद, आपकी रोज़ की दिनचर्या यह है:

1. **Docker Desktop शुरू करें** - ऐप खोलें और हरे स्टेटस इंडिकेटर की प्रतीक्षा करें (Docker चल रहा होना चाहिए)
2. **VS Code खोलें** - VS Code लॉन्च करें और अपना प्रोजेक्ट फ़ोल्डर खोलें
3. **Container में फिर से खोलें** - यदि पहले से container में नहीं हैं, तो हरे आइकन (नीचे-बाएँ) पर क्लिक करें और **Reopen in Container** चुनें
4. **कोड लिखें और चलाएँ** - `.py` फ़ाइलें एडिट करें, `Shift+Enter` से लाइन-दर-लाइन चलाएँ, या `streamlit run app.py` से ऐप चलाएँ
5. **अपना काम सेव करें** - आपकी कोड फ़ाइलें (`.py`, `.ipynb`) आपके कंप्यूटर में सेव होती हैं और सेशन के बाद भी बनी रहती हैं
6. **कमिट और पुश करें** - अपने बदलाव कमिट करने और रिपॉज़िटरी में पुश करने के लिए GitHub Desktop का उपयोग करें

---

निर्माता: [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/), 7 दिसंबर, 2025।
