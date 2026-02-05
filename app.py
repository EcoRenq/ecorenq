import streamlit as st

# Sayt ayarları
st.set_page_config(page_title="ecoRenq.az", page_icon="🌳", layout="wide")

# Yaddaş sistemi (Faylları burada saxlayacağıq)
if 'submissions' not in st.session_state:
    st.session_state.submissions = []
if 'page' not in st.session_state:
    st.session_state.page = "login"

# --- 1. İSTİFADƏÇİ GİRİŞİ ---
if st.session_state.page == "login":
    st.title("🌱 ecoRenq.az-a Xoş Gəldiniz")
    with st.form("user_info"):
        ad = st.text_input("Ad")
        soyad = st.text_input("Soyad")
        email = st.text_input("Email")
        submit = st.form_submit_button("Daxil Ol")
        if submit and ad and email:
            st.session_state.user = f"{ad} {soyad}"
            st.session_state.page = "main"
            st.rerun()

# --- 2. ANA SƏHİFƏ (Fayl Yükləmə) ---
elif st.session_state.page == "main":
    st.header(f"🌳 Xoş gəldiniz, {st.session_state.user}")
    
    st.subheader("📤 Materialları Yükləyin")
    img1 = st.file_uploader("Şəkil 1 (JPG/PNG)", type=['jpg', 'png'])
    vid = st.file_uploader("Video (MP4)", type=['mp4'])
    
    if st.button("Təbiət üçün Göndər 🚀"):
        if img1 or vid:
            # Məlumatı bazaya (yaddaşa) əlavə edirik
            data = {
                "istifadeci": st.session_state.user,
                "foto": img1,
                "video": vid
            }
            st.session_state.submissions.append(data)
            st.success("Məlumatlar göndərildi!")
            st.balloons()
        else:
            st.warning("Zəhmət olmasa ən azı bir fayl seçin.")

    # --- ADMİN PANELİ (SİZİN ÜÇÜN) ---
    st.sidebar.title("🔐 Admin Girişi")
    admin_pass = st.sidebar.text_input("Şifrə", type="password")
    
    if admin_pass == "eco2026":
        st.sidebar.success("Giriş uğurludur!")
        st.divider()
        st.header("📋 Gələn Məlumatlara Baxış")
        
        if not st.session_state.submissions:
            st.info("Hələ ki, heç kim fayl göndərməyib.")
        else:
            for i, item in enumerate(st.session_state.submissions):
                with st.expander(f"Göndərən: {item['istifadeci']}"):
                    if item['foto']:
                        st.image(item['foto'], caption="Göndərilən Şəkil", width=300)
                    if item['video']:
                        st.video(item['video'])
                    
                    # Xal vermə hissəsi
                    score = st.slider(f"Xal ver ({item['istifadeci']})", 0, 100, key=f"s_{i}")
                    if st.button(f"Xalı Təsdiqlə", key=f"b_{i}"):
                        st.toast(f"{item['istifadeci']} üçün {score} xal qeyd edildi!")

    # Footer
    st.divider()
    st.write("📸 [Instagram](https://www.instagram.com/ecorenq.az?igsh=Y2RnMGVjNXZiMTFl/)")
