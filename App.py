# ======================================================================
# Filename: app.py
# This is the complete script to run the Non-Human Persona Generator
# on your local computer.
# ======================================================================

# --- 1. Import necessary libraries ---
import streamlit as st
import google.generativeai as genai

# --- 2. Configure the page ---
# Set the title and icon that appear in the browser tab.
st.set_page_config(
    page_title="Non-Human Persona Generator",
    page_icon="🐾",
    layout="centered"
)

# --- 3. App Title and Description ---
# Display the main title and a caption on the page.
st.title("🐾 Non-Human Persona Generator")
st.caption("A tool to create detailed personas for non-human species using Google Gemini AI.")

# --- 4. API Key Input ---
# Create a password-style text input for the user to securely enter their API key.
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- 5. Main Application Logic ---
# The rest of the app will only run if an API key has been entered.
if api_key:
    # --- 5a. Configure the AI Model ---
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.success("API Key accepted! You can now generate a persona.", icon="✅")

        # --- 5b. Define the Prompt Generation Function ---
        # This function takes a species name and creates the detailed prompt for the AI.
        def get_prompt(species_name):
            return f"""
            Act as an expert ecologist and a creative designer. Create a detailed and well-structured 'Non-Human Persona' for the following species.
            Format the output using Markdown, and use bolding for key points.

            **Species Name:** {species_name}
            ---
            ### 1. Habitat
            - **Core Activity Space:** Where does this species primarily live, nest, and forage?
            - **Environmental Preferences:** What specific micro-habitats does it prefer or avoid?

            ### 2. Role in Ecosystem
            - **Primary Contribution:** What is its most significant contribution to the ecosystem?
            - **Food Web Position:** Who does it prey on? Who preys on it?

            ### 3. Core Needs
            - **Food:** What are its primary food sources?
            - **Water:** How does it access water?
            - **Shelter:** What kind of shelter or nest does it need?

            ### 4. Threats
            - **Primary Dangers:** What are the biggest threats to its survival?
            - **Human Impact:** Focus on threats from human activity.

            ### 5. Traces & Signs
            - **Observable Signs:** How can we tell this species has been here?

            ### 6. Design Suggestions
            - **Guiding Principle:** Propose a core design principle to help this species.
            - **Actionable Interventions:** Propose at least 3 specific, actionable design interventions.
            """

        # --- 5c. Set up the User Interface Elements ---
        # Create a text input for the user to enter the species name.
        species_input = st.text_input("Enter the species name you want to study:", placeholder="e.g., Red Panda")

        # Create a button to trigger the generation.
        if st.button("✨ Generate Persona"):
            if not species_input:
                st.warning("Please enter a species name first.")
            else:
                # Show a spinner while the AI is working.
                with st.spinner(f"Crafting a persona for the '{species_input}'..."):
                    try:
                        # Generate the prompt
                        prompt = get_prompt(species_input)
                        # Call the AI model
                        response = model.generate_content(prompt)
                        # Display the result
                        st.markdown("---")
                        st.markdown(response.text)
                    except Exception as e:
                        st.error(f"An error occurred while communicating with the AI: {e}")

    except Exception as e:
        # If the API key is invalid, show an error message.
        st.error(f"API Key authentication failed. Please check your key. Error details: {e}")
else:
    # If no API key is entered, show a prompt.
    st.info("Please enter your Google AI API Key above to start the application.")