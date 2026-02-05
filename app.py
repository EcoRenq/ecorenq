import streamlit as st

# Saytın əsas ayarları
st.set_page_config(page_title="ecoRenq.az", page_icon="🌳", layout="wide")

# Arxa plan dizaynı
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.85), rgba(255, 255, 255, 0.85)), 
        url("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=2026&auto=format&fit=crop");
        background-size: cover;
    }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Məlumat bazası (müvəqqəti yaddaş)
if 'db' not in st.session_state: st.session_state.db = []
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- GİRİŞ VƏ QEYDİYYAT ---
if not st.session_state.logged_in:
    st.title("🌱 ecoRenq.az-a Xoş Gəldiniz")
    with st.container():
        ad = st.text_input("Adınız")
        soyad = st.text_input("Soyadınız")
        yas = st.number_input("Yaşınız", min_value=1, max_value=100, value=20)
        email = st.text_input("Email ünvanınız")
        if st.button("Sistemə Daxil Ol"):
            if ad and soyad and email:
                st.session_state.current_user = {"ad": ad, "soyad": soyad, "yas": yas}
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Zəhmət olmasa bütün məlumatları doldurun!")

# --- ANA SƏHİFƏ ---
else:
    st.header(f"🌳 Salam, {st.session_state.current_user['ad']}!")
    
    # Sponsorlar üçün yer
    st.info("🤝 **SPONSORLAR:** Bura loqolar əlavə olunacaq")
    
    st.divider()
    
    # İSTƏDİYİN YÜKLƏMƏ SIRASI
    st.subheader("📤 Materialları Yükləyin")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        f1 = st.file_uploader("📸 1-ci Şəkil", type=['jpg', 'png'], key="img1")
    with col2:
        v1 = st.file_uploader("🎥 1-ci Video", type=['mp4', 'mov'], key="vid1")
    with col3:
        f2 = st.file_uploader("📸 2-ci Şəkil", type=['jpg', 'png'], key="img2")

    if st.button("Məlumatları Göndər 🚀"):
        new_entry = {
            "user": f"{st.session_state.current_user['ad']} {st.session_state.current_user['soyad']}",
            "yas": st.session_state.current_user['yas'],
            "files": [f1, v1, f2]
        }
        st.session_state.db.append(new_entry)
        st.success("Təbrik edirik! Uğurla göndərildi.")
        st.balloons()

    # --- ADMİN PANELİ (Sidebar-da şifrə yazılan kimi açılır) ---
    st.sidebar.title("🔐 Admin Girişi")
    sifre = st.sidebar.text_input("Şifrəni daxil edin", type="password")
    
    if sifre == "eco2026":
        st.sidebar.success("Admin girişi aktivdir!")
        st.divider()
        st.header("📋 Gələn Müraciətlər (Şəxsi Baxış)")
        
        if not st.session_state.db:
            st.info("Hələ ki, məlumat daxil olmayıb.")
        else:
            for i, entry in enumerate(st.session_state.db):
                with st.expander(f"👤 {entry['user']} - {entry['yas']} yaş"):
                    # Faylları göstər
                    c1, c2, c3 = st.columns(3)
                    if entry['files'][0]: c1.image(entry['files'][0], caption="Şəkil 1")
                    if entry['files'][1]: c2.video(entry['files'][1])
                    if entry['files'][2]: c3.image(entry['files'][2], caption="Şəkil 2")
                    
                    # 1000 BALLIQ SKALA
                    xal = st.select_slider(f"Xal ver: {entry['user']}", options=range(0, 1001), key=f"slider_{i}")
                    if st.button(f"Xalı Təsdiqlə", key=f"btn_{i}"):
                        st.toast(f"{entry['user']} üçün {xal} xal yadda saxlanıldı!")

    # --- FOOTER (ƏLAQƏ) ---
    st.divider()
    foot1, foot2 = st.columns(2)
    foot1.markdown(f"📞 [WhatsApp-la Əlaqə](https://wa.me/994998595659)")
    foot2.markdown(f"📸 [Instagram Səhifəmiz](https://www.instagram.com/ecorenq.az?igsh=Y2RnMGVjNXZiMTFl/)")
