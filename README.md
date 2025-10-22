# ATS Resume Expert

An Applicant Tracking System (ATS) that analyzes resumes against job descriptions using Google's Generative AI.

## Features

- **Resume Analysis**: Get detailed feedback on resume strengths and weaknesses
- **ATS Match Percentage**: Calculate how well a resume matches a job description
- **PDF Processing**: Upload and analyze PDF resumes
- **AI-Powered Insights**: Uses Google's Gemini AI for intelligent analysis

## Setup Instructions

### 1. Install Dependencies

```bash
# Install required packages
pip install streamlit google-generativeai python-dotenv pdf2image pillow

# Or install from requirements.txt
pip install -r requirements.txt
```

### 2. Get Google API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

### 3. Configure Environment

Create a `.env` file in the project directory:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

### 4. Run the Application

```bash
# Run the Streamlit app
streamlit run app.py
```

## Usage

1. **Enter Job Description**: Paste the job description in the text area
2. **Upload Resume**: Upload a PDF resume file
3. **Choose Analysis**:
   - "Tell Me About the Resume" - Get detailed feedback
   - "Percentage match" - Get ATS match percentage

## Files

- `app.py` - Main Streamlit application
- `simple_app.py` - Simplified command-line version (no dependencies)
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create this file)

## Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install missing packages with `pip install package_name`
2. **API Key Error**: Make sure your Google API key is correctly set in `.env`
3. **PDF Processing Error**: Ensure `pdf2image` and `pillow` are installed

### Alternative: Use Simple Version

If you have dependency issues, you can use the simplified version:

```bash
python simple_app.py
```

This version works without external dependencies but provides placeholder responses.

## Requirements

- Python 3.8+
- Google API Key
- Internet connection (for AI analysis)

## Notes

- The application requires a valid Google API key to function
- PDF processing works best with standard PDF formats
- Large PDF files may take longer to process
