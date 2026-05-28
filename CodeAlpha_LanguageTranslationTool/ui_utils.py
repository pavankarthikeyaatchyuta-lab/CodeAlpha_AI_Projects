import streamlit as st

def apply_custom_css(app_type="translator"):
    # Theme configuration
    themes = {
        "translator": {
            "bg_grad": "radial-gradient(circle at 50% 50%, #160d2e 0%, #05020c 100%)",
            "accent_color": "#00d2ff",
            "btn_grad": "linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%)",
            "btn_glow": "rgba(0, 201, 255, 0.3)",
            "btn_glow_hover": "rgba(0, 201, 255, 0.5)",
            "btn_grad_hover": "linear-gradient(90deg, #00d4ff 0%, #a2ffad 100%)",
        },
        "chatbot": {
            "bg_grad": "radial-gradient(circle at 50% 50%, #081220 0%, #02060b 100%)",
            "accent_color": "#00f0ff",
            "btn_grad": "linear-gradient(90deg, #00f0ff 0%, #7000ff 100%)",
            "btn_glow": "rgba(0, 240, 255, 0.3)",
            "btn_glow_hover": "rgba(0, 240, 255, 0.5)",
            "btn_grad_hover": "linear-gradient(90deg, #33f4ff 0%, #8c33ff 100%)",
        },
        "music": {
            "bg_grad": "radial-gradient(circle at 50% 50%, #1b0724 0%, #040108 100%)",
            "accent_color": "#ff007f",
            "btn_grad": "linear-gradient(90deg, #ff007f 0%, #7f00ff 100%)",
            "btn_glow": "rgba(255, 0, 127, 0.3)",
            "btn_glow_hover": "rgba(255, 0, 127, 0.5)",
            "btn_grad_hover": "linear-gradient(90deg, #ff3399 0%, #9933ff 100%)",
        },
        "vision": {
            "bg_grad": "radial-gradient(circle at 50% 50%, #05140b 0%, #010403 100%)",
            "accent_color": "#00ff80",
            "btn_grad": "linear-gradient(90deg, #00ff80 0%, #c4ff00 100%)",
            "btn_glow": "rgba(0, 255, 128, 0.3)",
            "btn_glow_hover": "rgba(0, 255, 128, 0.5)",
            "btn_grad_hover": "linear-gradient(90deg, #33ff99 0%, #cfff33 100%)",
        }
    }
    
    theme = themes.get(app_type, themes["translator"])
    
    # Show active layer CSS rule
    active_layer_rule = ""
    if app_type == "translator":
        active_layer_rule = ".stApp .animation-grid-3d { display: block !important; }"
    elif app_type == "chatbot":
        active_layer_rule = ".stApp .orb-1, .stApp .orb-2 { display: block !important; }"
    elif app_type == "music":
        active_layer_rule = ".stApp .animation-music-rings { display: block !important; }"
    elif app_type == "vision":
        active_layer_rule = ".stApp .animation-laser-sweep { display: block !important; }"

    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

        :root {{
            --bg-grad: {theme['bg_grad']};
            --accent-color: {theme['accent_color']};
            --btn-grad: {theme['btn_grad']};
            --btn-glow: {theme['btn_glow']};
            --btn-glow-hover: {theme['btn_glow_hover']};
            --btn-grad-hover: {theme['btn_grad_hover']};
        }}
        
        /* Base Theme */
        .stApp {{
            background: var(--bg-grad) !important;
            color: #e0e6ed;
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        
        /* Typography overrides */
        h1, h2, h3, h4, h5, h6 {{
            color: #ffffff !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px;
        }}

        /* Glassmorphism Containers */
        .glass-container {{
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 24px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
            transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1), border 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            z-index: 1;
            position: relative;
            animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
        }}
        
        .glass-container:hover {{
            transform: translateY(-5px);
            box-shadow: 0 20px 40px 0 rgba(0, 0, 0, 0.6), 0 0 15px var(--btn-glow);
            border: 1px solid var(--accent-color) !important;
        }}

        /* Animations */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(25px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        /* Glowing accents */
        .glow-text {{
            text-shadow: 0 0 20px var(--btn-glow);
            color: var(--accent-color) !important;
        }}

        /* Streamlit Element Overrides */
        /* Buttons */
        .stButton > button {{
            background: var(--btn-grad);
            color: #000000 !important;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px var(--btn-glow);
            width: 100%;
        }}
        
        .stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px var(--btn-glow-hover);
            background: var(--btn-grad-hover);
            color: #000 !important;
        }}

        /* Inputs */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div {{
            background: rgba(0, 0, 0, 0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            color: white !important;
            border-radius: 12px !important;
        }}
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > div:focus {{
            border-color: var(--accent-color) !important;
            box-shadow: 0 0 0 1px var(--btn-glow) !important;
        }}

        /* Chat UI */
        .stChatMessage {{
            background: transparent;
        }}
        [data-testid="chatAvatarIcon-user"] {{
            background-color: var(--accent-color);
        }}
        [data-testid="chatAvatarIcon-assistant"] {{
            background-color: #ff007f;
        }}
        .stChatMessage[data-testid="chat-message-user"] {{
             background: rgba(0, 210, 255, 0.05);
             border-radius: 12px;
             border: 1px solid rgba(0, 210, 255, 0.1);
        }}
        .stChatMessage[data-testid="chat-message-assistant"] {{
             background: rgba(255, 0, 127, 0.05);
             border-radius: 12px;
             border: 1px solid rgba(255, 0, 127, 0.1);
        }}

        /* File Uploader */
        [data-testid="stFileUploadDropzone"] {{
            background: rgba(255, 255, 255, 0.01) !important;
            border: 2px dashed rgba(255, 255, 255, 0.08) !important;
            border-radius: 16px !important;
        }}
        [data-testid="stFileUploadDropzone"]:hover {{
            border-color: var(--accent-color) !important;
            background: rgba(0, 210, 255, 0.02) !important;
        }}
        
        /* Floating animations */
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-8px); }}
            100% {{ transform: translateY(0px); }}
        }}
        .floating-element {{
            animation: float 6s ease-in-out infinite;
        }}

        /* Sidebar */
        [data-testid="stSidebar"] {{
            background-color: rgba(11, 15, 25, 0.96);
            border-right: 1px solid rgba(255, 255, 255, 0.05);
            z-index: 100;
        }}

        /* BACKGROUND 3D ANIMATIONS */
        .bg-animation-container {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -1;
            pointer-events: none;
            overflow: hidden;
        }}
        
        /* 3D Grid Animation (translator) */
        .animation-grid-3d {{
            display: none;
            position: absolute;
            top: -50%; left: -50%; right: -50%; bottom: -50%;
            background-image: 
                linear-gradient(rgba(0, 210, 255, 0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 210, 255, 0.04) 1px, transparent 1px);
            background-size: 60px 60px;
            transform: perspective(600px) rotateX(60deg) translateY(0);
            animation: gridMove 25s linear infinite;
        }}
        @keyframes gridMove {{
            from {{ transform: perspective(600px) rotateX(60deg) translateY(0); }}
            to {{ transform: perspective(600px) rotateX(60deg) translateY(60px); }}
        }}

        /* Drifting Orbs Animation (chatbot) */
        .animation-orbs {{
            display: none;
            position: absolute;
            border-radius: 50%;
            filter: blur(120px);
            opacity: 0.15;
        }}
        .orb-1 {{
            width: 500px; height: 500px;
            background: #00d2ff;
            top: 15%; left: 10%;
            animation: orbFloat 25s infinite ease-in-out;
        }}
        .orb-2 {{
            width: 600px; height: 600px;
            background: #7f00ff;
            bottom: 10%; right: 10%;
            animation: orbFloat 30s infinite ease-in-out;
            animation-delay: -10s;
        }}
        @keyframes orbFloat {{
            0%, 100% {{ transform: translate(0, 0) scale(1); }}
            50% {{ transform: translate(120px, 80px) scale(1.15); }}
        }}

        /* Pulsing rings (music) */
        .animation-music-rings {{
            display: none;
            position: absolute;
            top: 50%; left: 50%;
            width: 600px; height: 600px;
            margin-left: -300px; margin-top: -300px;
            border: 2px solid rgba(255, 0, 127, 0.03);
            border-radius: 50%;
            box-shadow: 
                0 0 120px rgba(255, 0, 127, 0.02),
                inset 0 0 120px rgba(127, 0, 255, 0.02);
            animation: ringPulse 8s infinite ease-in-out;
        }}
        @keyframes ringPulse {{
            0%, 100% {{ transform: scale(0.75); opacity: 0.15; }}
            50% {{ transform: scale(1.25); opacity: 0.75; }}
        }}

        /* Laser sweep (vision) */
        .animation-laser-sweep {{
            display: none;
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: 
                linear-gradient(rgba(0, 255, 128, 0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 128, 0.02) 1px, transparent 1px);
            background-size: 40px 40px;
        }}
        .animation-laser-sweep::after {{
            content: '';
            position: absolute;
            top: -10%; left: 0; right: 0; height: 8px;
            background: linear-gradient(to bottom, transparent, rgba(0, 255, 128, 0.15), transparent);
            box-shadow: 0 0 25px rgba(0, 255, 128, 0.3);
            animation: laserScan 6s linear infinite;
        }}
        @keyframes laserScan {{
            0% {{ top: -10%; }}
            100% {{ top: 110%; }}
        }}

        /* Inject Active Layer Rules */
        {active_layer_rule}
        </style>
        
        <div class="bg-animation-container">
            <div class="animation-grid-3d"></div>
            <div class="animation-orbs orb-1"></div>
            <div class="animation-orbs orb-2"></div>
            <div class="animation-music-rings"></div>
            <div class="animation-laser-sweep"></div>
        </div>
    """, unsafe_allow_html=True)

def render_glass_card(title, content, height="auto"):
    st.markdown(f"""
        <div class="glass-container" style="height: {height};">
            <h3 class="glow-text" style="margin-top: 0;">{title}</h3>
            <div style="color: #cbd5e1;">{content}</div>
        </div>
    """, unsafe_allow_html=True)

def render_header(title, subtitle):
    st.markdown(f"""
        <div style='text-align: center; padding: 2rem 0; animation: fadeInUp 0.8s ease-out;'>
            <h1 style='font-size: 3.5rem; margin-bottom: 0.5rem; background: linear-gradient(135deg, var(--accent-color) 0%, #ffffff 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: "Outfit", sans-serif; font-weight: 800; display: inline-block;' class='floating-element'>{title}</h1>
            <p style='color: #94a3b8; font-size: 1.2rem; letter-spacing: 1px; font-family: "Outfit", sans-serif;'>{subtitle}</p>
        </div>
        <hr style="border-color: rgba(255,255,255,0.05); margin-bottom: 3rem;">
    """, unsafe_allow_html=True)
