import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "Wang_Yuxinyi_Resume_English.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Jane_Doe_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Wang Yuxinyi")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** Antoniawang1204@163.com
    - **Phone:** (86)17743045330
    - **WeChat:** 18647396800
    - **QQ:** 1977370134
    """)

    st.header("Work Experience")
    st.markdown("""
    ### Macro Group Intern
    **Caitong Securities Research Institute.** | *June 2024 - September 2024*
    
    - Data Visualization and Analysis: Utilized iFind, Wind, Fred, and other overseas databases to gather data and create charts. Updated macroeconomic forecasts, monthly reports, and participated in the framework development of in-depth reports, covering U.S. commercial real estate, U.S. bond yields, U.S. inflation data, U.S. fiscal policy, U.S. and EU elections, and European economy.
    - Report Writing: Assisted in completing over 10 major research reports, including Emerging Markets — Focus on India, Emerging Markets — Focus on Vietnam, U.S. Credit Risk Series, Argentina Reforms, U.S. Financial Crisis Series, Review of U.S. Tax Reform, Interpretation of U.S. July Inflation Data, U.S. Election Policy Tracking, etc. Also wrote 6 briefings for clients and was responsible for daily news updates on the Middle East and Southeast Asia.
    """)
    
    st.markdown("""
    ### Operations Management Specialist
    **Xinxing Casting Co., Ltd.** | *February 2023 - September 2023*
    
    - E-commerce Marketing: Managed Alibaba International Platform, created promotional videos highlighting product advantages, analyzed user paths and conversion data using traffic management tools, optimized product details and targeted customer ads, resulting in a 20% increase in store visits and a 10% increase in paid conversions.
    -  Customer Development: Leveraged social media to identify potential customers, interacted with clients to understand their needs, explained product benefits, and completed tasks such as quotations, sample provision, shipping, and payment, bringing over 20,000 RMB in sales.
    """)
    
    st.markdown("""
    ### Research Assistant
    **Shanghai (Fudan University) Consumer Market Big Data Research Center** | *June 2022 - August 2022*
    
    - Data Analysis: Wrote Python scripts to scrape data on Shanghai's Qingming Festival foot traffic, the survival rate of 986 stores, and the Wuwu Shopping Street, cleaned and visualized the data using QGIS.
    - Report Writing: Conducted fieldwork with over 300 economic entities to understand their business operations. Wrote an analysis report on Shanghai's local consumer market trends, including foot traffic, store distribution, and other aspects, providing policy recommendations to the Shanghai Municipal Commercial Department and strategies for enterprises to adjust production.

    """)

    st.header("Education")
    st.markdown("""
     ### Master of Science in Marketing
    **The Chinese University of HongKong** | *August 2024 - July 2025*
    
    - GPA: 3.9/4.0
    - Track: Big Data 
    """)

    st.header("Skills")
    st.markdown("""
     Technical Skills
        - **Programming Languages:** Python, R
        - **Data Processing:** Pandas, NumPy
        - **Visualization:** Matplotlib, QGIS
        - **E-commerce Platforms:** Alibaba International Platform
        - **Cloud Platforms:** Google Cloud
    """)


    st.header("Languages")
    st.markdown("""
    - **English:** Native
    """)

    st.header("Interests")
    st.markdown("""
    - Blogging about technology trends
    """)

    st.markdown("---") 