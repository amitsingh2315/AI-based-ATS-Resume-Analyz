#!/usr/bin/env python3
"""
Test script to verify Google AI API and available models
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

def test_google_ai():
    print("🔍 Testing Google AI API...")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key or api_key == "your_google_api_key_here":
        print("❌ Google API Key: Not configured")
        return False
    
    print(f"✅ Google API Key: Found (ending with ...{api_key[-4:]})")
    
    try:
        # Configure the API
        genai.configure(api_key=api_key)
        print("✅ Google AI: Configured successfully")
        
        # List available models
        print("\n📋 Available Models:")
        models = list(genai.list_models())
        for model in models:
            print(f"  - {model.name}")
        
        # Test a simple model
        print("\n🧪 Testing model...")
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content("Hello, this is a test.")
            print("✅ Model test: Success")
            print(f"Response: {response.text[:100]}...")
        except Exception as e:
            print(f"❌ Model test failed: {e}")
            return False
        
        print("\n🎉 Google AI is working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Google AI Configuration failed: {e}")
        return False

if __name__ == "__main__":
    test_google_ai()
