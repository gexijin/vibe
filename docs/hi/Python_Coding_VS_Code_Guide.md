---
title: "VS Code में Python कोडिंग"
lang: "hi"
---
[होम](./)

# VS Code में Python कोडिंग

आप Python कोड लिखना चाहते हैं लेकिन तय नहीं कर पा रहे कि कौन-सा एडिटर उपयोग करें, या आप PyCharm से हल्का कुछ ढूँढ रहे हैं। VS Code को एक स्विस आर्मी नाइफ़ की तरह सोचें - यह एक ही हल्के एडिटर में Python, R, JavaScript, और कई अन्य भाषाओं को संभालता है। यह ट्यूटोरियल आपको दिखाता है कि कोड कम्प्लीशन, इंटरैक्टिव डीबगिंग, और यहाँ तक कि वेब ऐप जैसे स्मार्ट फ़ीचर के साथ VS Code में Python कैसे सेट अप करें।

## मुख्य अवधारणाएँ

- **[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)** - Microsoft का VS Code एक्सटेंशन जो सिंटैक्स हाइलाइटिंग, डीबगिंग, कोड निष्पादन, और Jupyter नोटबुक सपोर्ट प्रदान करता है
- **[Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)** - एक लैंग्वेज सर्वर जो Python के लिए तेज़ IntelliSense, टाइप चेकिंग, और ऑटो-इम्पोर्ट सक्षम करता है
- **[Virtual Environment](https://docs.python.org/3/library/venv.html)** - सिस्टम Python को प्रभावित किए बिना प्रोजेक्ट-विशिष्ट पैकेज प्रबंधित करने के लिए एक अलग Python एनवायरनमेंट
- **[Streamlit](https://streamlit.io/)** - सरल Python स्क्रिप्ट से इंटरैक्टिव वेब ऐप बनाने के लिए एक Python लाइब्रेरी

## आपको क्या चाहिए

- पूरा किया हुआ [VS Code Basics](./VS_Code_Getting_Started)
- Python और पैकेज डाउनलोड करने के लिए इंटरनेट कनेक्शन
- 15-20 मिनट

## चरण 1: Python इंस्टॉल करें

आधुनिक पैकेजों के साथ सर्वोत्तम संगतता के लिए आपको Python 3.8 या उससे ऊपर की ज़रूरत है।

- **Windows**:
  - [python.org](https://www.python.org/downloads/) से नवीनतम Python डाउनलोड करें
  - इंस्टॉलर चलाएँ
  - Install Now पर क्लिक करने से पहले **"Add python.exe to PATH" बॉक्स को चेक करें**
  - इंस्टॉलेशन स्थान नोट करें (आमतौर पर `C:\Users\YourName\AppData\Local\Programs\Python\Python312`)

- **macOS**:
  - [python.org](https://www.python.org/downloads/) से डाउनलोड करें और इंस्टॉलर चलाएँ
  - या Homebrew उपयोग करें: Terminal खोलें और `brew install python` टाइप करें
  - Homebrew पाथ: `/opt/homebrew/bin/python3` (Apple Silicon) या `/usr/local/bin/python3` (Intel)

- **Linux**:
  - Python आमतौर पर पहले से इंस्टॉल होता है। `python3 --version` से वर्शन जाँचें
  - यदि ज़रूरत हो, तो पैकेज मैनेजर से इंस्टॉल करें: `sudo apt install python3 python3-pip python3-venv` (Ubuntu/Debian)

एक terminal खोलकर और `python3 --version` या `python --version` टाइप करके इंस्टॉलेशन सत्यापित करें।

## चरण 2: VS Code में Python Extensions इंस्टॉल करें

- VS Code खोलें
- बाएँ साइडबार में **Extensions** आइकन पर क्लिक करें (या **View > Extensions** पर क्लिक करें)
- `ms-python.python` खोजें और Microsoft के Python extension पर **Install** क्लिक करें
- Pylance को Python extension के साथ अपने आप इंस्टॉल हो जाना चाहिए। यदि नहीं होता, तो `ms-python.vscode-pylance` खोजें और उसे इंस्टॉल करें

Python extension में डीबगिंग, IntelliSense, कोड फ़ॉर्मेटिंग, और Jupyter नोटबुक के लिए सपोर्ट शामिल है।

## चरण 3: अपना Python प्रोजेक्ट बनाएँ

- अपने कंप्यूटर पर एक नया फ़ोल्डर बनाएँ (जैसे, `my-python-project`)
- VS Code में, **File > Open Folder** पर क्लिक करें और अपना नया फ़ोल्डर चुनें
- ऊपर के मेनू में **File > New File** पर क्लिक करें
- फ़ाइल को **File > Save** पर क्लिक करके `analysis.py` के रूप में सेव करें

## चरण 4: Python इंटरप्रेटर चुनें

VS Code को यह जानना ज़रूरी है कि किस Python इंस्टॉलेशन का उपयोग करना है।

- मेनू बार में **View** पर क्लिक करें, फिर **Command Palette**
- `Python: Select Interpreter` टाइप करें और उसे चुनें
- आपने जो Python वर्शन इंस्टॉल किया है उसे चुनें (जैसे, `Python 3.12.x` या ऐसा ही कुछ)
- चुना गया इंटरप्रेटर VS Code के नीचे-दाएँ कोने में दिखता है

यदि आपको अपना Python इंस्टॉलेशन नहीं दिखता, तो **Enter interpreter path** पर क्लिक करें और वहाँ जाएँ जहाँ Python इंस्टॉल है।

## चरण 5: एक Virtual Environment बनाएँ

Virtual environment आपके प्रोजेक्ट की डिपेंडेंसी को अलग रखते हैं।

- मेनू बार में **View** पर क्लिक करें, फिर **Command Palette**
- `Python: Create Environment` टाइप करें और उसे चुनें
- **Venv** (बिल्ट-इन virtual environment) चुनें
- सूची से अपना Python इंटरप्रेटर चुनें
- VS Code के एनवायरनमेंट बनाने की प्रतीक्षा करें (आपको एक `.venv` फ़ोल्डर दिखेगा)
- VS Code आपके प्रोजेक्ट के लिए इस एनवायरनमेंट को अपने आप सक्रिय कर देगा

जब एनवायरनमेंट सक्रिय होगा तो आपको अपने terminal प्रॉम्प्ट में `(.venv)` दिखेगा।

## चरण 6: ज़रूरी पैकेज इंस्टॉल करें

- **View > Terminal** पर क्लिक करके VS Code में एक नया terminal खोलें
- terminal में `(.venv)` दिखना चाहिए, जो बताता है कि आपका virtual environment सक्रिय है
- ये कमांड टाइप करके पैकेज इंस्टॉल करें:

```bash
pip install pandas matplotlib streamlit
```

- इंस्टॉलेशन पूरा होने की प्रतीक्षा करें (1-2 मिनट लग सकते हैं)

यदि `(.venv)` नहीं दिखता, तो एनवायरनमेंट सक्रिय नहीं है। **View > Command Palette** पर क्लिक करें, `Python: Select Interpreter` चलाएँ, फिर वह इंटरप्रेटर चुनें जिसके साथ `('.venv': venv)` लिखा हो।

## चरण 7: अपनी पहली Python स्क्रिप्ट लिखें

`analysis.py` में यह कोड टाइप करें:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# View the first few rows
print(iris.head())

# Generate summary statistics
print("\nSummary Statistics:")
print(iris.describe())

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(iris['sepal_length'], bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')
plt.show()
```

- **File > Save** पर क्लिक करके फ़ाइल सेव करें

## चरण 8: Python कोड इंटरैक्टिव रूप से चलाएँ

- `analysis.py` खुला होने पर, ऊपर-दाएँ कोने में **▶ Run Python File** बटन पर क्लिक करें
- या एडिटर में राइट-क्लिक करें और **Run Python File in Terminal** चुनें
- terminal पैनल में आउटपुट आते देखें
- आपका प्लॉट दिखाने वाली एक हिस्टोग्राम विंडो पॉप अप होगी
- आप विशिष्ट लाइनें भी चुन सकते हैं और उन्हें एक इंटरैक्टिव Python सेशन में चलाने के लिए `Shift+Enter` दबा सकते हैं

## चरण 9: एक साधारण Streamlit ऐप बनाएँ

- एक नई फ़ाइल बनाएँ: **File > New File**
- इसे `app.py` के रूप में सेव करें
- यह कोड टाइप करें:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Histogram")

# Sidebar slider
bins = st.sidebar.slider(
    "Number of bins:",
    min_value=5,
    max_value=50,
    value=30
)

# Load data
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris = pd.read_csv(url)

# Create histogram
fig, ax = plt.subplots(figsize=(8, 6))
ax.hist(iris['sepal_length'], bins=bins, color='steelblue', edgecolor='white')
ax.set_xlabel('Sepal Length (cm)')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Sepal Length')

# Display in Streamlit
st.pyplot(fig)
```

- फ़ाइल सेव करें
- terminal खोलें और चलाएँ:

```bash
streamlit run app.py
```

- ऐप आपके ब्राउज़र में खुलता है (आमतौर पर `http://localhost:8501` पर)
- साइडबार में स्लाइडर हिलाएँ और हिस्टोग्राम को तुरंत अपडेट होते देखें
- ऐप रोकने के लिए terminal में `Ctrl+C` दबाएँ

## चरण 10: कोड कम्प्लीशन और IntelliSense का उपयोग करें

- `analysis.py` में, एक नई लाइन पर `iris.` टाइप करना शुरू करें
- सभी उपलब्ध मेथड और एट्रिब्यूट के साथ एक ड्रॉपडाउन दिखाई देता है
- `iris.gr` टाइप करें और देखें कि यह `groupby()` सुझाता है
- अपने मौजूदा कोड में `pd.read_csv` पर माउस घुमाएँ
- एक पॉपअप फ़ंक्शन सिग्नेचर, पैरामीटर, और दस्तावेज़ीकरण दिखाता है
- `import ` टाइप करने की कोशिश करें और देखें कि VS Code कैसे पैकेज नामों का सुझाव देता है
- जब आप कोई फ़ंक्शन कॉल टाइप करते हैं, तो IntelliSense पैरामीटर संकेत दिखाता है

## चरण 11: डीबगिंग आज़माएँ

- `analysis.py` में, ब्रेकपॉइंट सेट करने के लिए लाइन नंबर 8 (`print(iris.head())` वाली लाइन) के बाईं ओर क्लिक करें (एक लाल बिंदु दिखाई देगा)
- मेनू बार में **Run** पर क्लिक करें, फिर **Start Debugging**
- पूछे जाने पर **Python File** चुनें
- कोड निष्पादन ब्रेकपॉइंट पर रुक जाता है
- कोड में स्टेप-थ्रू करने, वेरिएबल जाँचने, और कॉल स्टैक देखने के लिए डीबग टूलबार का उपयोग करें
- निष्पादन जारी रखने के लिए **Run > Continue** पर क्लिक करें

## अगले कदम

- डेटा मैनिपुलेशन और विश्लेषण के लिए [pandas](https://pandas.pydata.org/) एक्सप्लोर करें
- इंटरैक्टिव डेटा साइंस के लिए VS Code में [Jupyter notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) सीखें
- वेब API बनाने के लिए [Flask](https://flask.palletsprojects.com/) या [FastAPI](https://fastapi.tiangolo.com/) आज़माएँ
- ऑटोमैटिक कोड फ़ॉर्मेटिंग के लिए [Black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) इंस्टॉल करें
- टेस्ट लिखने और चलाने के लिए [pytest](https://docs.pytest.org/) का उपयोग करें

## समस्या निवारण

- **terminal में "Python is not recognized"**: Python आपके सिस्टम PATH में नहीं है। Windows पर, Python फिर से इंस्टॉल करें और "Add python.exe to PATH" चेक करें। Mac/Linux पर, `python` की बजाय `python3` का उपयोग करें। ठीक करने के बाद VS Code रीस्टार्ट करें।

- **कोई इंटरप्रेटर नहीं मिला**: VS Code के नीचे-दाएँ कोने में इंटरप्रेटर सिलेक्टर पर क्लिक करें, या **View > Command Palette** पर क्लिक करके `Python: Select Interpreter` चलाएँ। यदि आपका Python इंस्टॉलेशन नहीं दिखता, तो **Enter interpreter path** चुनें और अपनी Python एक्ज़ीक्यूटेबल फ़ाइल तक ब्राउज़ करें।

- **Virtual environment सक्रिय नहीं हो रहा**: जब आप terminal खोलते हैं तो VS Code को इसे अपने आप सक्रिय कर देना चाहिए। यदि नहीं होता, तो मैन्युअल रूप से सक्रिय करें: Windows: `.venv\Scripts\activate`, Mac/Linux: `source .venv/bin/activate`। अपने terminal प्रॉम्प्ट में `(.venv)` देखकर सत्यापित करें।

- **IntelliSense काम नहीं कर रहा**: सुनिश्चित करें कि Pylance इंस्टॉल और सक्षम है। जाँचें कि नीचे-दाएँ कोने में आपका चुना हुआ इंटरप्रेटर दिख रहा है। Pylance को शुरू होने के लिए फ़ाइल खोलने के बाद 10-20 सेकंड प्रतीक्षा करें। समस्या बनी रहने पर VS Code रीस्टार्ट करें।

- **pip install विफल होता है**: सुनिश्चित करें कि आपका virtual environment सक्रिय है (terminal में `(.venv)` देखें)। Linux पर, आपको पहले `python3-venv` इंस्टॉल करने की ज़रूरत हो सकती है। Windows पर, जाँचें कि एंटीवायरस pip को ब्लॉक नहीं कर रहा।

- **Streamlit ऐप नहीं चलता**: सुनिश्चित करें कि streamlit आपके virtual environment में इंस्टॉल है (`pip list | grep streamlit`)। त्रुटि संदेशों के लिए terminal जाँचें। सुनिश्चित करें कि कोई अन्य ऐप पोर्ट 8501 का उपयोग नहीं कर रहा।

## वर्कफ़्लो सारांश

VS Code इन फ़ायदों के साथ Python डेवलपमेंट के लिए एक आधुनिक, हल्का एनवायरनमेंट प्रदान करता है:

- **एकीकृत एनवायरनमेंट**: एक ही एडिटर में Python, R, JavaScript, और अधिक कोड करें
- **शक्तिशाली IntelliSense**: Pylance के ज़रिए स्मार्ट कम्प्लीशन, टाइप चेकिंग, और ऑटो-इम्पोर्ट
- **इंटीग्रेटेड डीबगिंग**: ब्रेकपॉइंट सेट करें, वेरिएबल जाँचें, और कोड में स्टेप-थ्रू करें
- **Jupyter सपोर्ट**: अलग ऐप्लिकेशन के बिना सीधे VS Code में नोटबुक चलाएँ
- **वर्शन कंट्रोल**: बदलावों को ट्रैक करने के लिए बिल्ट-इन Git इंटीग्रेशन
- **एक्सटेंशन इकोसिस्टम**: टेस्टिंग, फ़ॉर्मेटिंग, लिंटिंग, और अधिक के लिए हज़ारों एक्सटेंशन

---

निर्माता: [Steven Ge](https://www.linkedin.com/in/steven-ge-ab016947/), 7 दिसंबर, 2025।
