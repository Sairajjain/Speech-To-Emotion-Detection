import speech_recognition as sr
import text2emotion as te
import nltk
import streamlit as st

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('punkt_tab')

def record_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak something to analyze emotion:")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("🔍 Recognizing...")
        text = r.recognize_google(audio)
        print("📝 You said:", text)
        return text
    except sr.UnknownValueError:
        print("😕 Could not understand audio")
        return ""
    except sr.RequestError:
        print("⚠️ Error connecting to Google API")
        return ""

def detect_emotion(text):
    if text:
        emotion = te.get_emotion(text)
        st.write(emotion)
        for i in emotion.keys():
            if emotion[i]!=0:
                st.info(f'major emotions in context is :- {i} with :- {emotion[i]}')
        print("💡 Detected Emotion:", emotion)
    else:
        print("❌ No text to analyze.")

if __name__ == "__main__":
    st.title('😎speech to emotion detection😒')
    a=st.button('Record')
    if a:
        st.write('🎤 Speak something to analyze emotion:')
        st.write("🔍 Recognizing...")
        text = record_speech()
        st.write('📝 You said:',text)
        detect_emotion(text)
