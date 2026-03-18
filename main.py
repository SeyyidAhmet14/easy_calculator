import streamlit as st

st.title("🧮 Basit Hesap Makinesi")

# --- SIDEBAR ---
st.sidebar.header("İşlemi Belirle")

sayi1 = st.sidebar.number_input("Birinci sayı", value=0)
sayi2 = st.sidebar.number_input("İkinci sayı", value=0)

islem = st.sidebar.selectbox("İşlem seç:", ["Toplama", "Çıkarma", "Çarpma", "Bölme"])


# --- SONUÇ ---
st.write("## Sonuç:")

if islem == "Toplama":
    st.write(sayi1 + sayi2)
elif islem == "Çıkarma":
    st.write(sayi1 - sayi2)
elif islem == "Çarpma":
    st.write(sayi1 * sayi2)
else:
    if sayi2 != 0:
        st.write(sayi1 / sayi2)
    else:
        st.error("0'a bölme yapılamaz!")
