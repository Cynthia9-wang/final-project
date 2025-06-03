import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
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
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "E-commerce Marketing Optimization",
            "description": "Optimized product listings and promotional content on Alibaba International Platform to improve user engagement and conversion rates.",
            "skills": ["Python", "Data Analysis", "User Path Analysis", "Funnel Analysis"],
            "outcome": "Increased store visits by 20% and paid conversions by 10%, generating over 20,000 RMB in sales."
        },
        {
            "title": "Consumer Market Data Analysis",
            "description": "Collected and analyzed consumer market data in Shanghai using Python and QGIS to assess trends and provide insights for policy and strategy development.",
            "skills": ["Python", "QGIS", "Data Collection", "Data Visualization"],
            "outcome": "Produced a report that contributed to strategic policy-making for the Shanghai Municipal Commercial Department."
        },

    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R
        - **Data Processing:** Pandas, NumPy
        - **Visualization:** Matplotlib, QGIS
        - **E-commerce Platforms:** Alibaba International Platform
        - **Cloud Platforms:** Google Cloud
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Strong written and verbal communication skills
        - **Teamwork:** Collaborative team player with experience in cross-functional environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Adaptability:** Quick learner with the ability to thrive in dynamic environments
        """)
    
    st.markdown("---") 