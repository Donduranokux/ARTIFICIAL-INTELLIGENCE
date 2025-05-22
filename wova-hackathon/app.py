import streamlit as st
import openai

openai.api_key = "APIKEYGIZLENDI"

st.title("SmartIntern – AI Destekli Staj Adayı Analizi")
st.write("Formu doldurun, sistem sizi değerlendirsin.")

with st.form("adayi_degerlendir"):
    python = st.radio("Python biliyor musun?", ("Evet", "Hayır"))
    proje = st.radio("Daha önce proje geliştirdin mi?", ("Evet", "Hayır"))
    alan = st.selectbox("Hedeflediğin alan nedir?", ["Veri", "Web", "Yapay Zeka", "Diğer"])
    saat = st.slider("Haftalık kaç saat çalışabilirsin?", 0, 40, 10)
    ekip = st.radio("Ekip çalışmasında rahat mısın?", ("Evet", "Hayır"))
    gönder = st.form_submit_button("Analiz Et")

def skorla():
    puan = 0
    if python == "Evet":
        puan += 20
    if proje == "Evet":
        puan += 30
    if saat >= 10:
        puan += 20
    if ekip == "Evet":
        puan += 10
    return puan

def ai_oneri(puan, alan):
    prompt = f"""
    Bir aday başvurduğu alanda {puan} puan aldı. Hedef alanı: {alan}.
    Bu adaya gelişimi için 3 öneri ver.
    """
    yanit = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return yanit.choices[0].message.content

if gönder:
    puan = skorla()
    st.success(f"Toplam Puanınız: {puan}")
    st.info("Yapay Zekâ tarafından oluşturulan gelişim önerileri:")
    st.write(ai_oneri(puan, alan))
