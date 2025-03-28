import streamlit as st
from transformers import pipeline

# Initialize the local model (replace with your model path)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2") #or any other local model

generator = load_model()

def generate_response(prompt):
    """Generates a response using the local model."""
    try:
        response = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
        return response.strip()
    except Exception as e:
        return f"Error generating response: {e}"

def refine_preferences(prompt):
    """Refines user preferences with clarifying questions."""
    return generate_response(f"Refine the following travel request: {prompt}. Ask clarification questions about diet, interests, mobility, and accommodation.")

def suggest_activities(prompt):
    """Suggests activities based on location and preferences."""
    return generate_response(f"Suggest top attractions and activities for {prompt}, considering the user's preferences.")

def generate_itinerary(prompt):
    """Generates a detailed itinerary."""
    return generate_response(f"Generate a detailed, day-by-day itinerary for {prompt}.")

st.title("AI Travel Planner")

user_input = st.text_input("Enter your travel destination and preferences:")

if st.button("Get Travel Plan"):
    if user_input:
        # Step 1: Refine preferences
        refinement = refine_preferences(user_input)
        st.write("Refined Preferences:")
        st.write(refinement)

        # Step 2: Suggest activities
        activities = suggest_activities(user_input)
        st.write("Suggested Activities:")
        st.write(activities)

        # Step 3: Generate itinerary
        itinerary = generate_itinerary(user_input)
        st.write("Detailed Itinerary:")
        st.write(itinerary)
    else:
        st.write("Please enter your travel preferences.")