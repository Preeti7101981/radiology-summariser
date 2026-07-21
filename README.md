# Radiology Summariser

A Python-based specialized tool designed to summarize medical radiology reports into concise, actionable insights. This project leverages language models from the Hugging Face Hub to provide high-quality medical text summarization through a clean API interface.

## Features
- **Specialized Summarization:** Tailored for the clinical nuances of radiology reports.
- **Hugging Face Integration:** Uses state-of-the-art models with secure token authentication.
- **FastAPI / Flask Backend:** (Adjust based on your actual framework) Provides a lightweight API endpoint for processing reports.

## Prerequisites
- Python 3.8 or higher.
- A Hugging Face account and a [User Access Token](https://huggingface.co/settings/tokens).

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Preeti7101981/radiology-summariser.git
   cd radiology-summariser

  Install dependencies:
  pip install -r requirements.txt

  Configure environment variables
  # On Windows (Command Prompt)
set HUGGINGFACE_HUB_TOKEN=your_token_here

# On Windows (PowerShell)
$env:HUGGINGFACE_HUB_TOKEN="your_token_here"

# On Linux/macOS
export HUGGINGFACE_HUB_TOKEN=your_token_here

# Usage
Run the application using:
python api.py
The API will start locally, and you can send radiology report text to the defined endpoint for summarization.

# LICENSE
I have used the MIT License, which is the most popular choice for open-source portfolio projects on GitHub
MIT License

Copyright (c) 2026 Preeti7101981

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
