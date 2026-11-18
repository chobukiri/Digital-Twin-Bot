# app.py
import streamlit as st
import pandas as pd
from database import supabase
import design  # Import your custom UI module

# 1. Page Config (Must remain at the very top)
st.set_page_config(
    page_title="Gui Shi Jun | Digital Twin",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Inject UI from design.py
design.apply_styles()
design.render_hero()

# 3. Interactive Tabs
tab1, tab2, tab3 = st.tabs(["🚀 Live Code Vault", "📊 Command Analytics", "🛠️ Hardware & Stack"])

# --- TAB 1: YOUR GITHUB & CODE VAULT ---
with tab1:
    st.subheader("Latest Autonomous Pushes")
    
    # Fetch the 5 most recent pushes from your Supabase vault
    vault_response = supabase.table("code_vault").select("*").order("created_at", desc=True).limit(5).execute()
    
    if vault_response.data:
        for item in vault_response.data:
            # Create a clean dropdown UI for each commit/snippet
            with st.expander(f"📦 {item.get('language', 'Update')}"):
                st.write(item.get('ai_summary', ''))
                if item.get('code_snippet'):
                    st.code(item['code_snippet'])
    else:
        st.info("Vault is currently empty. Send a command in Discord to populate!")

# --- TAB 2: YOUR REAL-TIME CHART ---
with tab2:
    st.subheader("Discord Bot Telemetry")
    
    # Fetch all logged commands to build the dashboard
    analytics_response = supabase.table("analytics_log").select("*").execute()
    
    if analytics_response.data:
        df = pd.DataFrame(analytics_response.data)
        # Create a bar chart grouping the types of commands logged
        if 'event_type' in df.columns:
            st.bar_chart(df['event_type'].value_counts())
        else:
            st.dataframe(df) # Fallback view
    else:
        st.info("Awaiting telemetry data...")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 💻 Development Stack")
        st.write("- **Engines:** Unity (2022.3 LTS & Unity 6), Unreal Engine 5")
        st.write("- **Languages:** C#, C++, Python, Swift, SQL")
        st.write("- **Frameworks:** ARKit, RealityKit, Streamlit, Supabase")
    with col2:
        st.write("### ⚙️ Command Center Hardware")
        st.write("- **Primary Terminal:** Custom VS Code IDE (Windows)")
        st.write("- **Always-On Server Interface:** Repurposed iPhone 8")
        st.write("- **Mobile Webhook Alerts:** Galaxy S26 Ultra / iPad Mini 7")
        st.write("- **VR Testing Rig:** Meta Quest + Logitech G29")

