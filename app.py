import streamlit as st

from summarizer import generate_summary
from utils import extract_text_from_pdf

from audio_utils import (
    transcribe_audio,
    translate_text,     
    text_to_speech
)

st.set_page_config(
    page_title="AI Multilingual Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("AI Multilingual Summarizer")

st.write(
    "Upload TXT, PDF, or Audio files and generate translated summaries with audio output."
)

# -----------------------------------
# INPUT TYPE
# -----------------------------------

input_type = st.radio(
    "Choose Input Type",
    ["Text/PDF", "Audio"]
)

text = ""

# TEXT / PDF MODE

if input_type == "Text/PDF":

    summary_language = st.selectbox(
        "Summary Language",
        ["en", "hi", "fr", "es", "de"],
        key="text_summary_language"
    )

    uploaded_file = st.file_uploader(
        "Upload a TXT or PDF file",
        type=["txt", "pdf"]
    )

    if uploaded_file is not None:

        if uploaded_file.type == "text/plain":
            text = uploaded_file.read().decode("utf-8")

        elif uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)

    # DISPLAY TEXT

    if text:

        st.subheader("Original / Processed Text")

        with st.expander("View Text"):
            st.write(text)

        if st.button("Generate Summary"):

            with st.spinner("Generating summary..."):

                summary = generate_summary(text)

            if summary_language != "en":

                with st.spinner(
                    f"Translating summary to {summary_language}..."
                ):

                    summary = translate_text(
                        summary,
                        summary_language
                    )

            st.subheader("Summary")
            st.write(summary)

            with st.spinner("Generating audio..."):

                audio_file = text_to_speech(
                    summary,
                    summary_language
                )

            st.subheader("Summary Audio")
            st.audio(audio_file)

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

    else:
        st.info("Please upload a valid file.")

# AUDIO MODE

elif input_type == "Audio":

    uploaded_audio = st.file_uploader(
        "Upload Audio File",
        type=["mp3", "wav", "m4a"]
    )

    input_language = st.selectbox(
        "Input Language",
        ["en", "hi", "fr", "es", "de"],
        key="audio_input_language"
    )

    summary_language = st.selectbox(
        "Summary Language",
        ["en", "hi", "fr", "es", "de"],
        key="audio_summary_language"
    )

    if uploaded_audio is not None:

        st.audio(uploaded_audio)

        if st.button("Generate Summary"):

            # TRANSCRIBE

            with st.spinner("Transcribing audio..."):

                transcribed_text = transcribe_audio(
                    uploaded_audio
                )

            if transcribed_text.startswith("Error"):

                st.error(transcribed_text)
                st.stop()

            # SUMMARIZE

            with st.spinner("Generating summary..."):

                summary = generate_summary(
                    transcribed_text
                )

            # TRANSLATE

            if summary_language != "en":

                with st.spinner(
                    f"Translating summary to {summary_language}..."
                ):

                    summary = translate_text(
                        summary,
                        summary_language
                    )

            # AUDIO OUTPUT

            with st.spinner("Generating audio..."):

                audio_file = text_to_speech(
                    summary,
                    summary_language
                )

            st.subheader("Summary Audio")
            st.audio(audio_file)

            st.download_button(
                label="Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

    else:
        st.info("Please upload a valid audio file.")