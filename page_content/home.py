import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Wang Yuxinyi</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:Antoniawang1204@163.com">Antoniawang1204@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image2.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a Master’s student in Marketing at The Chinese University of Hong Kong, with a solid foundation in business analysis and data visualization. My internship experience includes roles at Caitong Securities Research Institute, Xinxing Casting Co., Ltd., and Fudan University’s Consumer Market Research Center, where I developed skills in data analysis, market research, and e-commerce marketing. I am passionate about content creation and team leadership, as shown by my role as Deputy Head at Jilin University TV Station. Proficient in both English and Mandarin, I am eager to apply my skills in dynamic business environments.
        """
    )

    st.markdown(
        """
       ### Skills
        - **Programming Languages:** Python, R
        - **Data Processing:** Pandas, NumPy
        - **Visualization:** Matplotlib, QGIS
        - **E-commerce Platforms:** Alibaba International Platform
        - **Cloud Platforms:** Google Cloud
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 