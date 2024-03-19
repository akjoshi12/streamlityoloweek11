import streamlit as st

st.header(" Third 👁️ Eye Innovative Team ")

st.write("--------------------------------------")

# # Team member data (replace with your actual data)
team_members = [
    {"image": "Profiles/sameer.jpeg", "name": "Sameer Sharma", "role": "Team Lead", "tagline": "Third Eye"},
    {"image": "Profiles/shubham.jpeg", "name": "Shubham Bhavsar", "role": "Machine Learning Lead", "tagline": "Third Eye"},
    {"image": "Profiles/Atri_joshi.jpeg", "name": "Atri Joshi", "role": "Data Lead", "tagline": "Third Eye"},
    {"image": "Profiles/ayesha.jpeg", "name": "Ayesha Quereshi", "role": "UI/Documentation", "tagline": "Third Eye"},
    {"image": "Profiles/janvi.jpeg", "name": "Janvi Rai", "role": "UI/Documentation", "tagline": "Third Eye"},
    {"image": "Profiles/palash.jpeg", "name": "Palash Lalani", "role": "ML Engineer", "tagline": "Third Eye"},
    {"image": "Profiles/sucheta.jpeg", "name": "Sucheta Adhikarey", "role": "UI/Documentation", "tagline": "Third Eye"},
    {"image": "Profiles/marmik.jpeg", "name": "Marmik Upadhayay", "role": "UI Developer", "tagline": "Third Eye"},
    {"image": "Profiles/aman.jpeg", "name": "Aman Belwal", "role": "UI Developer", "tagline": "Third Eye"},
    {"image": "Profiles/kundan.jpeg", "name": "Kundan Singh", "role": "UI", "tagline": "Third Eye"},
    {"image": "Profiles/shekhar.jpeg", "name": "Shekhar Tiruwa", "role": "ML Engineer", "tagline": "Third Eye"},
    {"image": "Profiles/yash.jpeg", "name": "Yash Mahendra", "role": "ML Engineer", "tagline": "Third Eye"},
    {"image": "Profiles/sumith.jpeg", "name": "Sumith Vadla", "role": "UI Developer", "tagline": "Third Eye"},
    {"image": "Profiles/Dhanush.jpeg", "name": "Dhanush", "role": "ML Engineer", "tagline": "Third Eye"},






   
]

cols = 4

def create_team_card(member):
    """Creates a Streamlit card for each team member"""
    st.write(f"**{member['name']}**")
    st.image(member['image'], width=150)
    st.write(f"{member['role']}")
    st.write(f"{member['tagline']}")
    st.write("---")
# Display team members in a grid layout
num_rows = (len(team_members) + cols - 1) // cols
row_counter = 0
for i in range(num_rows):
    row_counter += 1
    cols_in_row = min(cols, len(team_members) - (i * cols))
    inner_columns = st.columns(cols_in_row)

    for j in range(cols_in_row):
        member_index = (i * cols) + j
        with inner_columns[j]:
            create_team_card(team_members[member_index])
    if row_counter < num_rows:
        st.write("---")  # Add horizontal line between rows

st.write("We are passionate about building innovative solutions. Get to know our amazing team!")
