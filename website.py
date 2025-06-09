import streamlit as st


about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)



pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)



st.sidebar.markdown("Made by [Hamidur](https://www.facebook.com/hamidur0x)")


pg.run()
