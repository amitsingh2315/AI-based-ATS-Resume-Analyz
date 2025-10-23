import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

# Configure Google AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt):
    try:
        # Get available models and find one that supports vision
        available_models = list(genai.list_models())
        vision_models = [model for model in available_models if 'image' in model.name.lower() or 'vision' in model.name.lower()]
        
        # Try vision models first, then fallback to general models
        model_names = []
        if vision_models:
            model_names.extend([model.name for model in vision_models[:3]])
        model_names.extend(['gemini-pro-latest', 'gemini-flash-latest'])
        
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content([input_text, pdf_content[0], prompt])
                return response.text
            except Exception as model_error:
                st.warning(f"Model {model_name} failed: {str(model_error)[:100]}...")
                continue
        
        # If all models fail, return a helpful error
        st.error("All Google AI models failed. Please check your API key and try again.")
        return "Error: Unable to process request with any available model."
        
    except Exception as e:
        st.error(f"Error calling Google AI: {e}")
        return f"Error: Unable to process request. {str(e)}"

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Read the file bytes once and use them
            pdf_bytes = uploaded_file.read()
            
            # When deployed on Render (after Step 1), this will work
            images = pdf2image.convert_from_bytes(pdf_bytes)
            
            # Check if images were created
            if not images:
                st.error("Could not convert PDF to image. The file might be corrupted or empty.")
                return None
                
            first_page = images[0]

            # Convert to bytes
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
                }
            ]
            return pdf_parts
        
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
            st.error("Please ensure Poppler is installed on the server and the PDF file is not corrupted.")
            return None
    else:
        raise FileNotFoundError("No file uploaded")
            
## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")


input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

# This "if" starts at the far left
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response=get_gemini_response(input_prompt1,pdf_content,input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Failed to process PDF. Please check the file and try again.")
    else:
        st.write("Please upload the resume")

# This "elif" must ALSO start at the far left
elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        if pdf_content is not None:
            response=get_gemini_response(input_prompt3,pdf_content,input_text)
            st.subheader("The Response is")
            st.write(response)
        else:
            st.error("Failed to process PDF. Please check the file and try again.")
    else:
        st.write("Please upload the resume")



    
