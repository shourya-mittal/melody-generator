from melodygenerator import app_run
import streamlit as st
import os

def main():
    # Set page configuration (using a clean layout and title)
    st.set_page_config(page_title="Melody Generator", page_icon="🎵", layout="centered")

    # Custom CSS for cyberpunk theme
    st.markdown("""
                
        <style>
            /* General background and text colors */
            body {
                background-color:  #820300;
                color: #820300;
            }
            
            /* Heading and title styles */
            .css-16d1e3t {
                color: #00b8d9;
                font-weight: bold;
                font-size: 36px;
            }
            
            .css-1vj2sc4 {
                color: #ff00f7;
            }
            
            /* File uploader button */
            .css-1emrehy {
                background-color: #7f00ff;
                color: #ffffff;
                font-weight: bold;
            }
            
            /* File uploader hover effect */
            .css-1emrehy:hover {
                background-color: #ff00f7;
                color: #121212;
            }
            
            /* Subheader styling */
            .css-1v0mbdj {
                color: #7f00ff;
            }
            
            /* Success message color */
            .css-1gwf3wr {
                background-color: #00b8d9;
                color: #121212;
            }
            
            /* Footer text */
            .footer {
                text-align: center;
                color: #ff00f7;
                font-size: 14px;
                padding: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and intro text
    st.title("Melody Generator")
    st.markdown("""
        **Welcome to the Melody Generator.**  
        Upload a MIDI file below to generate/continue it.
    """)

    # Styling the file uploader widget with custom design
    st.subheader("Upload your MIDI file")
    midi_file = st.file_uploader("Choose a MIDI file", type=["mid", "midi"])

    if midi_file is not None:
        # Save the uploaded file locally in a dedicated directory
        save_dir = "uploaded_files"
        file_path = os.path.join(save_dir, midi_file.name)
        os.makedirs(save_dir, exist_ok=True)
        
        # Save the uploaded file to disk
        with open(file_path, "wb") as f:
            f.write(midi_file.getbuffer())
        
        # Success message with elegant styling
        st.success(f"File '{midi_file.name}' is being processed.")

        # Display file info in a neat format
        st.markdown(f"**File Information:**")
        st.write(f"- **File name**: `{midi_file.name}`")
        st.write(f"- **File size**: {midi_file.size / 1024:.2f} KB")
        
        st.write("Your melody shall load in MuseScore soon")
        # Call the custom function with the saved file path
        app_run(file_path)

    # Add a footer with some credits or additional information
    st.markdown("""
        <div class="footer">
            This tool was created by Aniket, Shourya and Aman.  
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()