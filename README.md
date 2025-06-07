# AI-text-completion-app
# Generative AI Text Completion App

**Authored by Joshith Reddy**

## Overview
This project demonstrates how to build a simple text completion application using the Hugging Face Inference API. You will learn to prompt a pre-trained language model, adjust generation parameters, and evaluate output quality.

## Prerequisites
- Python 3.8 or higher
- A Hugging Face account and API token
- Basic familiarity with command-line interfaces

## Setup
1. **Clone this repository**  
2. **Navigate** to the project directory  
3. **Create** a virtual environment  
   ```bash
   python -m venv venv
   ```
4. **Activate** the environment  
   - **PowerShell**:  
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```  
   - **Command Prompt**:  
     ```cmd
     venv\Scripts\activate.bat
     ```  
5. **Install** dependencies  
   ```bash
   pip install huggingface_hub python-dotenv
   ```

## Configuration
Create a file named `.env` in the repository root and add:
```
HF_TOKEN=hf_your_api_token_here
```

## Usage
Run the application:
```bash
python app.py
```
- **Prompt:** Enter your text prompt.
- **Temperature:** Controls randomness (0.0 = deterministic, 1.0 = default).
- **max_new_tokens:** Limits generated length.
- Type `exit` or `quit` to terminate.

## Experimentation
Sample prompts and responses are logged in `experimentation_log.xlsx`. Review this file to analyze:
- Coherence and relevance
- Impact of temperature and token limits
- Model behavior across domains

## Limitations
- **Repetition & Drift:** May repeat or go off-topic on long outputs.
- **Factual Accuracy:** Simplifies or misstates facts without grounding.
- **Logical Consistency:** Struggles with multi-step reasoning.
- **Hallucinations:** Can generate incorrect or fabricated details.

## Future Improvements
- Integrate **retrieval-augmented generation** for fact grounding.
- Add **output filtering** and **fact-checking** modules.
- Develop a **web interface** for better user experience.
