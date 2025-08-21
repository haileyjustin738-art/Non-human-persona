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
        # --- 5b. Define the NEW Prompt Generation Function (KEY CHANGE HERE!) ---
        # This function has been completely rewritten to produce friendlier, more actionable content.
        def get_prompt(species_name):
            return f"""
            Act as a friendly community ecologist and outreach coordinator. Your mission is to create a guide for community residents about the species "{species_name}". The tone should be extremely simple, friendly, and inspiring.

            **Strictly follow the format instructions for every section below:**
            For each of the five sections, you must respond using **a few concise bullet points, with a single-sentence explanation following each point.**

            ---

            ### 1. Where can we find it near us?
            *Goal: Tell residents where to look in plain, simple language.*
            *Format: 2-3 concise points + a one-sentence explanation for each.*
            *(e.g., "On old park trees: because they love to make their nests in high tree cavities.")*

            ### 2. Why is it a good neighbor?
            *Goal: Explain its benefits to the local environment to build a positive connection.*
            *Format: 2-3 concise points + a one-sentence explanation for each.*
            *(e.g., "It eats mosquitoes: a single bat can eat hundreds of insects in one night, acting as a natural pest controller.")*

            ### 3. What does it need to thrive in our community?
            *Goal: Help residents understand its basic survival needs.*
            *Format: 2-3 concise points + a one-sentence explanation for each.*
            *(e.g., "A clean, shallow water source: it needs a place to drink and clean itself safely.")*

            ### 4. What dangers does it face in our neighborhood?
            *Goal: Point out specific threats related to residential life to foster empathy.*
            *Format: 2-3 concise points + a one-sentence explanation for each.*
            *(e.g., "Bright decorative lights: excessive light at night can disorient it, making it hard to find its way home.")*

            ### 5. What simple things can we do to help?
            *Goal: Provide super simple, actionable tips that residents can do right at their doorstep.*
            *Format: 3 specific, actionable points + a one-sentence explanation for each.*
            *(e.g., "Leave a pile of leaves in a corner of the yard: this provides a winter home for it and the insects it eats.")*
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