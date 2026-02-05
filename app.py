import streamlit as st

# Sayt ayarları
st.set_page_config(page_title="ecoRenq.az", page_icon="🌿", layout="wide")

# CSS - Yaşıl dizayn və Şriftlər
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 50, 0, 0.7), rgba(0, 50, 0, 0.7)), 
        url("https://images.unsplash.com/photo-1511497584788-8767fe771d21?q=80&w=1932&auto=format&fit=crop");
        background-size: cover; color: white;
    }
    .main-card { background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border: 1px solid #4CAF50; }
    h1, h2, h3 { color: #4CAF50 !important; font-family: 'Arial'; }
    .stButton>button { background-color: #2e7d32 !important; color: white !important; border-radius: 20px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Yaddaş Sistemi (Qeyd: Müvəqqəti yaddaş hələlik eyni serverdə qalır)
if 'db' not in st.session_state: st.session_state.db = []
if 'page' not in st.session_state: st.session_state.page = "login"

# --- 1. QEYDİYYAT SƏHİFƏSİ ---
if st.session_state.page == "login":
    st.markdown("<h1 style='text-align: center;'>🌿 ecoRenq.az</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>Təbiəti qoru, xal qazan, hədiyyə al! Sən də bizlərə qoşul!</p>", unsafe_allow_html=True)
    
    with st.container():
        col_l, col_r = st.columns(2)
        with col_l:
            ad = st.text_input("Adınız")
            soyad = st.text_input("Soyadınız")
        with col_r:
            yas = st.number_input("Yaşınız", 5, 100, 20)
            email = st.text_input("Email")
            
        if st.button("HƏRƏKƏTƏ KEÇ 🚀"):
            if ad and soyad and email:
                st.session_state.current_user = {"ad": ad, "soyad": soyad, "yas": yas}
                st.session_state.page = "main"
                st.rerun()

# --- 2. ANA SƏHİFƏ ---
elif st.session_state.page == "main":
    st.title(f"🌳 Salam, {st.session_state.current_user['ad']}!")
    
    # SPONSOR BÖLMƏSİ
    st.markdown("<div style='background: rgba(76, 175, 80, 0.2); padding: 15px; border-radius: 10px; text-align: center; border: 1px dashed #4CAF50;'>"
                "<h3>🤝 SƏN DƏ BİZLƏRƏ QOŞUL!</h3><p>Sponsorluq və tərəfdaşlıq üçün bizimlə əlaqə saxlayın.</p></div>", unsafe_allow_html=True)
    
    st.divider()

    # YÜKLƏMƏ SIRASI: 1 Şəkil + 1 Video + 1 Şəkil
    st.subheader("📤 Eko-Fəaliyyətini Bizimlə Paylaş")
    c1, c2, c3 = st.columns(3)
    with c1: f1 = st.file_uploader("📸 Şəkil 1", type=['jpg', 'png'], key="u1")
    with c2: v1 = st.file_uploader("🎥 Video", type=['mp4', 'mov'], key="u2")
    with c3: f2 = st.file_uploader("📸 Şəkil 2", type=['jpg', 'png'], key="u3")

    if st.button("MƏLUMATI GÖNDƏR 🌍"):
        if f1 or v1 or f2:
            st.session_state.db.append({
                "ad": st.session_state.current_user['ad'],
                "soyad": st.session_state.current_user['soyad'],
                "yas": st.session_state.current_user['yas'],
                "fayllar": [f1, v1, f2]
            })
            st.success("Möhtəşəm! Məlumatlarınız yadda saxlanıldı.")
            st.balloons()

    # --- ADMİN PANELİ (SİZİN ÜÇÜN ŞƏXSİ) ---
    st.sidebar.markdown("## 🔐 Admin Girişi")
    sifre = st.sidebar.text_input("Şifrə", type="password")
    
    if sifre == "eco2026":
        st.sidebar.success("Xoş gəldin, Rəhbər!")
        st.header("📋 Gələn Eko-Fəaliyyətlər")
        
        if not st.session_state.db:
            st.info("Hələ ki, yeni məlumat yoxdur.")
        else:
            for i, item in enumerate(st.session_state.db):
                with st.expander(f"👤 {item['ad']} {item['soyad']} ({item['yas']} yaş)"):
                    sc1, sc2, sc3 = st.columns(3)
                    if item['fayllar'][0]: sc1.image(item['fayllar'][0], width=200)
                    if item['fayllar'][1]: sc2.video(item['fayllar'][1])
                    if item['fayllar'][2]: sc3.image(item['fayllar'][2], width=200)
                    
                    # 1000 BALLIQ SKALA
                    st.markdown("### 🎯 Qiymətləndirmə")
                    bal = st.select_slider(f"Xal (0-1000)", options=range(0, 1001), key=f"bal_{i}")
                    if st.button(f"Xalı Təsdiqlə", key=f"btn_{i}"):
                        st.toast(f"{item['ad']} üçün {bal} xal verildi!")

    # FOOTER
    st.divider()
    fcol1, fcol2 = st.columns(2)
    fcol1.markdown("📞 [WhatsApp: +994 99 859 56 59](https://wa.me/994998595659)")
    fcol2.markdown("📸 [Instagram: @ecorenq.az](https://www.instagram.com/ecorenq.az?igsh=Y2RnMGVjNXZiMTFl/)")    
