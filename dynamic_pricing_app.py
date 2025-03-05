import streamlit as st

# Custom CSS for Blue Background & Bold Text
page_bg_img = '''
<style>
.stApp {
    background: linear-gradient(135deg, #1E3C72, #2A5298);  /* Blue Gradient */
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Sidebar Styling */
[data-testid="stSidebar"] {
    background-color: rgba(10, 25, 47, 0.9); /* Dark Blue Sidebar */
}

/* Text and Input Styling */
h1, h2, h3, h4, h5, h6, label, .stTextInput, .stNumberInput, .stSelectbox {
    color: white !important;
    font-weight: bold;
}

/* Bold and Large Text */
.bold-text {
    font-size: 22px;
    font-weight: bold;
    color: white;
}

/* Highlighted Price Box */
.price-box {
    font-size: 28px;
    font-weight: bold;
    color: #FFD700; /* Gold Color */
    background: rgba(255, 255, 255, 0.2); /* Transparent White */
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.8);
}

/* Button Styling */
.stButton>button {
    background-color: #00A8E8;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px;
    transition: 0.3s;
    border: none;
}

.stButton>button:hover {
    background-color: #0077B6;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# 🚀 Dynamic Pricing Engine UI
st.title("Dynamic Pricing Engine")
st.subheader("🌍 Adjust the parameters to predict ride pricing")

# Input fields
riders = st.number_input("🧑‍🤝‍🧑 Number of Riders", min_value=1, step=1)
drivers = st.number_input("🚖 Number of Drivers", min_value=1, step=1)
past_rides = st.number_input("🛣 Number of Past Rides", min_value=0, step=1)
ratings = st.slider("⭐ Average Ratings", min_value=0.0, max_value=5.0, step=0.1)
duration = st.number_input("⏳ Expected Ride Duration (minutes)", min_value=1, step=1)

# Dropdown selections
location = st.selectbox("📍 Location Category", ["Urban", "Suburban", "Rural"])
loyalty = st.selectbox("🎖 Customer Loyalty Status", ["Regular", "VIP", "New"])
time_of_booking = st.selectbox("⏰ Time of Booking", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("🚗 Vehicle Type", ["Standard", "Premium", "Luxury"])

# Display selected inputs with BOLD and LARGE text
st.markdown(f"""
<div class="bold-text">
📊 <b>Selected Parameters:</b><br>
✅ <b>Riders:</b> {riders} &nbsp;&nbsp; ✅ <b>Drivers:</b> {drivers} &nbsp;&nbsp; ✅ <b>Past Rides:</b> {past_rides}<br>
⭐ <b>Ratings:</b> {ratings} &nbsp;&nbsp; ⏳ <b>Duration:</b> {duration} min<br>
📍 <b>Location:</b> {location} &nbsp;&nbsp; 🎖 <b>Loyalty Status:</b> {loyalty}<br>
⏰ <b>Time:</b> {time_of_booking} &nbsp;&nbsp; 🚗 <b>Vehicle Type:</b> {vehicle}
</div>
""", unsafe_allow_html=True)

# Predict button
if st.button("🔮 Predict Price"):
    estimated_price = round(riders * duration * 1.5, 2)
    st.markdown(f'<div class="price-box">🚕 Estimated Price: ₹{estimated_price}</div>', unsafe_allow_html=True)
