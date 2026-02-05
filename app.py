import streamlit as st

# Sayt ayarları
st.set_page_config(page_title="ecoRenq.az", page_icon="🌳", layout="wide")

# Arxa plan və dizayn (Mənzərəli CSS)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), 
        url("https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?q=80&w=2026&auto=format&fit=crop");
        background-size: cover;
        background-attachment: fixed;
    }
    .main-box { background-color: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 15px; border: 2px solid #2e7d32; }
    </style>
    """, unsafe_allow_html=True)

# Yaddaş
if 'submissions' not in st.session_state: st.session_state.submissions = []
if 'page' not in st.session_state: st.session_state.page = "login"

# --- 1. GİRİŞ SƏHİFƏSİ ---
if st.session_state.page == "login":
    st.title("🌱 ecoRenq.az-a Xoş Gəldiniz")
    st.write("### Təbiəti birlikdə qoruyaq!")
    with st.form("user_info"):
        ad = st.text_input("Ad")
        soyad = st.text_input("Soyad")
        yas = st.number_input("Yaş", min_value=5, max_value=100)
        email = st.text_input("Email")
        submit = st.form_submit_button("Daxil Ol")
        if submit and ad and email:
            st.session_state.user = f"{ad} {soyad}"
            st.session_state.yas = yas
            st.session_state.page = "main"
            st.rerun()

# --- 2. ANA SƏHİFƏ ---
elif st.session_state.page == "main":
    st.header(f"🌳 Xoş gəldiniz, {st.session_state.user} ({st.session_state.yas} yaş)")
    
    # SPONSORLAR ÜÇÜN BOŞ YER
    st.info("🤝 **SPONSORLARIMIZ:** (Bura sponsor loqoları əlavə olunacaq)")
    # 
    
    st.divider()

    st.subheader("📤 Materialları Yükləyin")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("🖼️ **Şəkillər (Cəmi 4 ədəd)**")
        img1 = st.file_uploader("1-ci Şəkil", type=['jpg', 'png'], key="i1")
        img2 = st.file_uploader("2-ci Şəkil", type=['jpg', 'png'], key="i2")
        img3 = st.file_uploader("3-cü Şəkil", type=['jpg', 'png'], key="i3")
        img4 = st.file_uploader("4-cü Şəkil", type=['jpg', 'png'], key="i4")

    with col2:
        st.write("🎥 **Videolar (Cəmi 2 ədəd)**")
        vid1 = st.file_uploader("1-ci Video", type=['mp4', 'mov'], key="v1")
        vid2 = st.file_uploader("2-ci Video", type=['mp4', 'mov'], key="v2")

    if st.button("Təbiət üçün Göndər 🚀"):
        # Məlumatı bazaya əlavə edirik
        data = {
            "istifadeci": st.session_state.user,
            "yas": st.session_state.yas,
            "fayllar": [img1, img2, img3, img4, vid1, vid2]
        }
        st.session_state.submissions.append(data)
        st.success("Təbrik edirik! Materiallar uğurla qəbul edildi.")
        st.balloons()

    # --- ADMİN PANELİ ---
    st.sidebar.title("🔐 Admin Girişi")
    admin_pass = st.sidebar.text_input("Şifrə", type="password")
    
    if admin_pass == "salam2004":
        st.header("📋 Gələn Məlumatlar və 1000 Ballıq Skala")
        
        for i, item in enumerate(st.session_state.submissions):
            with st.expander(f"Göndərən: {item['istifadeci']} ({item['yas']} yaş)"):
                st.write("Yüklənən fayllara baxış:")
                # Faylları göstərmək üçün kiçik dövr
                for f in item['fayllar']:
                    if f:
                        if f.type.startswith('image'): st.image(f, width=200)
                        if f.type.startswith('video'): st.video(f)
                
                # 1000 BALLIQ SKALA
                score = st.select_slider(f"Xal ver ({item['istifadeci']})", options=range(0, 1001), key=f"s_{i}")
                if st.button(f"Xalı Təsdiqlə", key=f"b_{i}"):
                    st.success(f"{item['istifadeci']} üçün {score}/1000 xal verildi!")

    # Footer
    st.divider()
    st.write("📸 [Instagram](https://www.instagram.com/ecorenq.az?igsh=Y2RnMGVjNXZiMTFl/)")
