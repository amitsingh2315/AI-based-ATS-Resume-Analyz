#!/usr/bin/env python3
"""
Simple test script to check if all required packages are available
"""

try:
    import streamlit as st
    print("✓ Streamlit imported successfully")
except ImportError as e:
    print(f"✗ Streamlit import failed: {e}")

try:
    import google.generativeai as genai
    print("✓ Google Generative AI imported successfully")
except ImportError as e:
    print(f"✗ Google Generative AI import failed: {e}")

try:
    import pdf2image
    print("✓ pdf2image imported successfully")
except ImportError as e:
    print(f"✗ pdf2image import failed: {e}")

try:
    from PIL import Image
    print("✓ PIL (Pillow) imported successfully")
except ImportError as e:
    print(f"✗ PIL import failed: {e}")

try:
    import base64
    import io
    import os
    print("✓ Standard library modules imported successfully")
except ImportError as e:
    print(f"✗ Standard library import failed: {e}")

print("\nAll imports completed!")
