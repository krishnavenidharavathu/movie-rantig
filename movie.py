import streamlit as st
import google.generativeai as genai

def generate_movie_information(movie_name, genre, target_audience, main_actor):
    """Generates detailed movie information based on given parameters.

    Args:
        movie_name: The name of the movie.
        genre: The genre of the movie.
        target_audience: The target audience for the movie.
       
        main_actor: The main actor in the movie.
       
       

    Returns:
        A dictionary containing the detailed movie information, or None if an error occurs.
    """
    try:
        # Configure API key
        genai.configure(api_key="AIzaSyD2Qtu7c68RMORegyHreBMskB71o4Irn4o")

        # Create the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are a movie critic. Provide detailed movie information based on the given details including genre, target audience, director, main actor, release year, and plot description.",
        )

        # Construct the prompt
        prompt = (
            f"Provide detailed information for the movie '{movie_name}', which is a {genre} film aimed at {target_audience}. "
            f" and stars {main_actor}." 
          
            "Include a synopsis, key details, and any critical reception if available."
        )

        # Generate the movie information
        response = model.generate_content(prompt)
        info_text = response.text

        # Basic information formatting
        info_dict = {"info": ""}
        lines = info_text.split("\n")
        for line in lines:
            info_dict["info"] += line + "\n"

        return info_dict

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit UI
st.title("AI Movie Information Generator")

# Input fields
movie_name = st.text_input("Enter the name of the movie:")
genre = st.text_input("Enter the genre of the movie(e.g.Action,Love,Drama,Horror):")
target_audience = st.text_input("Enter the target audience for the movie(e.g.,Children,Family,Adults):")

main_actor = st.text_input("Enter the main actor in the movie:")



if st.button("Generate Information"):
    # Ensure required fields are not empty
    if not (movie_name and genre and target_audience  and main_actor ):
        st.error("Please fill in all the required fields.")
    else:
        info = generate_movie_information(movie_name, genre, target_audience,  main_actor)

        if info:
            st.header("Movie Information")
            st.write(info["info"])
        else:
            st.error("Failed to generate movie information.")
