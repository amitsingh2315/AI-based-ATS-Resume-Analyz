!/usr/bin/env python3
"""
Simplified ATS Resume Expert Application
This version works without external dependencies for testing
"""

import os
import base64
import io

def get_simple_response(input_text, pdf_content, prompt):
    """Simple response function that doesn't require Google AI"""
    return f"""
    ATS Analysis Results:
    
    Job Description: {input_text}
    
    Analysis: This is a placeholder response. To get real AI analysis, you need to:
    1. Install all required packages: pip install -r requirements.txt
    2. Get a Google API key from https://makersuite.google.com/app/apikey
    3. Add your API key to the .env file
    
    Prompt used: {prompt}
    
    Note: This is a demo version. The full version requires Google Generative AI API.
    """

def input_pdf_setup(uploaded_file):
    """Simplified PDF processing"""
    if uploaded_file is not None:
        # For demo purposes, just return a placeholder
        return [{"mime_type": "application/pdf", "data": "PDF_CONTENT_PLACEHOLDER"}]
    else:
        raise FileNotFoundError("No file uploaded")

def main():
    print("=" * 50)
    print("ATS Resume Expert - Simplified Version")
    print("=" * 50)
    
    # Get job description
    job_description = input("Enter job description: ")
    
    # Get resume file path
    resume_path = input("Enter resume file path (or press Enter to skip): ")
    
    if resume_path and os.path.exists(resume_path):
        print(f"✓ Resume file found: {resume_path}")
        
        # Simulate file upload
        class MockUploadedFile:
            def __init__(self, path):
                self.path = path
            def read(self):
                with open(self.path, 'rb') as f:
                    return f.read()
        
        uploaded_file = MockUploadedFile(resume_path)
        
        # Process PDF
        try:
            pdf_content = input_pdf_setup(uploaded_file)
            print("✓ PDF processed successfully")
        except Exception as e:
            print(f"✗ Error processing PDF: {e}")
            return
        
        # Analysis prompts
        prompt1 = """
        You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
        Please share your professional evaluation on whether the candidate's profile aligns with the role. 
        Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
        """
        
        prompt3 = """
        You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
        your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
        the job description. First the output should come as percentage and then keywords missing and last final thoughts.
        """
        
        # Get user choice
        print("\nChoose analysis type:")
        print("1. Resume Review")
        print("2. ATS Match Percentage")
        choice = input("Enter choice (1 or 2): ")
        
        if choice == "1":
            response = get_simple_response(job_description, pdf_content, prompt1)
            print("\n" + "=" * 50)
            print("RESUME REVIEW")
            print("=" * 50)
            print(response)
        elif choice == "2":
            response = get_simple_response(job_description, pdf_content, prompt3)
            print("\n" + "=" * 50)
            print("ATS MATCH ANALYSIS")
            print("=" * 50)
            print(response)
        else:
            print("Invalid choice")
    else:
        print("No valid resume file provided")
    
    print("\n" + "=" * 50)
    print("Analysis Complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()
