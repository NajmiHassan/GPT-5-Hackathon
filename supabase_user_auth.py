import streamlit as st
from supabase import create_client

# ---- CONFIG ----
SUPABASE_URL = "https://tcsqgrgmzitouqgnmciz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRjc3Fncmdteml0b3VxZ25tY2l6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU3MTk5MTUsImV4cCI6MjA3MTI5NTkxNX0.n89p9N76b6taA5houJZL-opvpA5ClX_r3gAYHkQsjkg"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---- SESSION STATE ----
if "user" not in st.session_state:
    st.session_state["user"] = None

# ---- FUNCTIONS ----
def sign_up(email, password):
    try:
        response = supabase.auth.sign_up({"email": email, "password": password})
        return response
    except Exception as e:
        return {"error": str(e)}

def sign_in(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if response.user:
            st.session_state["user"] = response.user
        return response
    except Exception as e:
        return {"error": str(e)}

def sign_out():
    try:
        supabase.auth.sign_out()
        st.session_state["user"] = None
    except Exception as e:
        st.error(f"Error signing out: {e}")

# ---- UI ----
st.title("🔐 Streamlit + Supabase Auth Example")

if st.session_state["user"] is None:
    # Login / Signup tabs
    tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

    with tab1:
        st.subheader("Sign In")
        email = st.text_input("Email", key="signin_email")
        password = st.text_input("Password", type="password", key="signin_password")
        if st.button("Sign In"):
            res = sign_in(email, password)
            if getattr(res, "user", None):
                st.success(f"Welcome back {res.user.email}!")
            else:
                st.error("Login failed")

    with tab2:
        st.subheader("Sign Up")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_password")
        if st.button("Sign Up"):
            res = sign_up(email, password)
            if getattr(res, "user", None):
                st.success("✅ Account created! Please check your email for confirmation.")
            else:
                st.error("Sign up failed")

else:
    st.success(f"✅ Logged in as {st.session_state['user'].email}")
    if st.button("Sign Out"):
        sign_out()
        st.info("You have been signed out.")










# Initialize the client in your Streamlit app

# import streamlit as st
# from supabase import create_client

# # ---- CONFIG ----
# SUPABASE_URL = "https://tcsqgrgmzitouqgnmciz.supabase.co"
# SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRjc3Fncmdteml0b3VxZ25tY2l6Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU3MTk5MTUsImV4cCI6MjA3MTI5NTkxNX0.n89p9N76b6taA5houJZL-opvpA5ClX_r3gAYHkQsjkg"
# supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# # ---- SESSION STATE ----
# if "user" not in st.session_state:
#     st.session_state["user"] = None

# # ---- FUNCTIONS ----
# def sign_up(email, password):
#     try:
#         response = supabase.auth.sign_up({"email": email, "password": password})
#         return response
#     except Exception as e:
#         return {"error": str(e)}

# def sign_in(email, password):
#     try:
#         response = supabase.auth.sign_in_with_password({"email": email, "password": password})
#         if response.user:
#             st.session_state["user"] = response.user
#         return response
#     except Exception as e:
#         return {"error": str(e)}

# def sign_out():
#     try:
#         supabase.auth.sign_out()
#         st.session_state["user"] = None
#     except Exception as e:
#         st.error(f"Error signing out: {e}")

# # ---- UI ----
# st.title("🔐 Streamlit + Supabase Auth Example")

# if st.session_state["user"] is None:
#     # Login / Signup tabs
#     tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

#     with tab1:
#         st.subheader("Sign In")
#         email = st.text_input("Email", key="signin_email")
#         password = st.text_input("Password", type="password", key="signin_password")
#         if st.button("Sign In"):
#             res = sign_in(email, password)
#             if getattr(res, "user", None):
#                 st.success(f"Welcome back {res.user.email}!")
#             else:
#                 st.error("Login failed")

#     with tab2:
#         st.subheader("Sign Up")
#         email = st.text_input("Email", key="signup_email")
#         password = st.text_input("Password", type="password", key="signup_password")
#         if st.button("Sign Up"):
#             res = sign_up(email, password)
#             if getattr(res, "user", None):
#                 st.success("Account created! Please check your email for confirmation.")
#             else:
#                 st.error("Sign up failed")

# else:
#     st.success(f"✅ Logged in as {st.session_state['user'].email}")
#     if st.button("Sign Out"):
#         sign_out()
#         st.info("You have been signed out.")
