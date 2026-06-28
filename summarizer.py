import streamlit as st
from transformers import pipeline

# LOAD MODEL (CACHED)

@st.cache_resource
def load_model():
    return pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )


summarizer = load_model()

# CHUNK TEXT

def chunk_text(text, chunk_size=150):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        chunks.append(chunk)

    return chunks


# GENERATE SUMMARY

def generate_summary(text):

    if not text or not text.strip():
        return "No text available for summarization."

    chunks = chunk_text(text)

    all_summaries = []  

    for chunk in chunks:

        try:

            # Skip very small chunks
            if len(chunk.split()) < 10:
                continue

            summary = summarizer(
                chunk,
                max_length=100,
                min_length=25,
                do_sample=False
            )

            if summary and len(summary) > 0:

                all_summaries.append(
                    summary[0]["summary_text"]
                )

        except Exception as e:

            print(f"Summarization Error: {e}")
            continue

    # Fallback 
    if not all_summaries:
        return "Unable to generate summary."

    final_summary = " ".join(all_summaries)

    return final_summary