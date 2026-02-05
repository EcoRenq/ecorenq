import streamlit as st

# --- SAYTIN AYARLARI ---
st.set_page_config(page_title="ecoRenq.az", layout="centered")

# Rəngləri və dizaynı gözəlləşdirək (CSS)
st.markdown("""
    <style>
    .main { background-color: #f0fdf4; }
    .stButton>button { background-color: #22c55e; color: white; border-radius: 10px; }
    .stProgress > div > div > div > div { background-color: #16a34a; }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state: st.session_state.step = "entry"
if 'user_score' not in st.session_state: st.session_state.user_score = 0

# --- 1. GİRİŞ SƏHİFƏSİ ---
if st.session_state.step == "entry":
    st.image("https://cdn-icons-png.flaticon.com/512/489/489969.png", width=80)
    st.title("🌱 ecoRenq.az-a Xoş Gəldiniz")
    with st.form("qeydiyyat"):
        ad = st.text_input("Ad")
        soyad = st.text_input("Soyad")
        email = st.text_input("Email")
        yas = st.number_input("Yaş", min_value=5, max_value=100)
        submit = st.form_submit_button("Daxil Ol")
        
        if submit:
            if ad and soyad and email:
                st.session_state.user_data = {"ad": ad, "soyad": soyad}
                st.session_state.step = "dashboard"
                st.rerun()
            else:
                st.error("Zəhmət olmasa bütün xanaları doldurun!")

# --- 2. MÜŞTƏRİ PANELİ ---
elif st.session_state.step == "dashboard":
    st.header(f"🌳 ecoRenq Dünyası: {st.session_state.user_data['ad']}")
    
    # Material Yükləmə
    st.subheader("📤 Paylaşım Et")
    c1, c2, c3 = st.columns(3)
    with c1: st.file_uploader("📸 Şəkil 1", type=['jpg', 'png'])
    with c2: st.file_uploader("🎥 Video", type=['mp4'])
    with c3: st.file_uploader("📸 Şəkil 2", type=['jpg', 'png'])
    
    if st.button("Təbiət üçün Göndər 🚀"):
        st.balloons()
        st.success("Təbrik edirik! ecoRenq olaraq paylaşımınızı qəbul etdik.")

    # Bal Skalası
    st.write(f"### Sizin Eco-Balınız: **{st.session_state.user_score} / 100**")
    st.progress(st.session_state.user_score)
    
    # Footer & Sosial Medya
    st.divider()
    sc1, sc2, sc3 = st.columns(3)
    st.write("📸 [Instagram](https://www.instagram.com/ecorenq.az?igsh=Y2RnMGVjNXZiMTFl/)")
    sc2.write("💬 [WhatsApp](https://wa.me/994998595659)")
    sc3.write("🤝 **Sponsorlar**: Sende bizlere qosulmaq isteyirsen")

    # --- 3. ADMİN PANELİ (GİZLİ) ---
    with st.sidebar:
        st.title("🔑 Admin")
        admin_pass = st.text_input("Şifrə", type="password")
        if admin_pass == "eco2026":
            st.write(f"Müştəri: {st.session_state.user_data['ad']}")
            yeni_bal = st.slider("Xal ver", 0, 100, st.session_state.user_score)
            if st.button("Balı Təsdiqlə"):
                st.session_state.user_score = yeni_bal
                st.rerun()
            if st.button("🎁 Hədiyyə Gönder"):
                st.toast("Hədiyyə müştəriyə bildirildi!")
