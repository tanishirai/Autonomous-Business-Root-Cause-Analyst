"""
The Autonomous Analytics Investigator Agent (Gemini Version).
Orchestrates the investigation workflow using Google's Gemini API.
"""
import os
import json
import traceback
import google.generativeai as genai
from dotenv import load_dotenv
from backend.models import InvestigationResponse
from agent.tools import AVAILABLE_TOOLS, get_metric_overview

# 1. Load environment variables from the .env file
load_dotenv()

# 2. Configure Gemini using the key from the .env file
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# 3. Initialize the model
model = genai.GenerativeModel('models/gemini-flash-latest')

SYSTEM_PROMPT = """
You are an expert Business Analytics Investigator. 
Your goal is to answer business questions using data, NOT by guessing.
You have access to analytical tools. You must use them to gather evidence before answering.

When you respond, you MUST output ONLY valid JSON matching this exact schema. 
Do not include markdown formatting like ```json ... ``` around the output. Just the raw JSON string.
{
  "executive_summary": "1-2 sentence summary of the findings.",
  "hypotheses_tested": [{"id": "H1", "description": "...", "test_method": "..."}],
  "evidence": [{"hypothesis_id": "H1", "metric": "...", "finding": "...", "quantitative_value": 0.0, "sample_size": 0, "confidence": "High"}],
  "root_causes": ["Root cause 1", "Root cause 2"],
  "recommendations": ["Actionable recommendation 1"],
  "limitations": "What the data cannot prove."
}
"""

def run_investigation(question: str) -> InvestigationResponse:
    """Main function to process a business question."""
    try:
        # 1. Gather initial context from our Python tools
        overview = get_metric_overview()
        context = f"Dataset Overview: {json.dumps(overview)}"
        
        tool_descriptions = "\n".join([f"- {name}: {desc['description']}" for name, desc in AVAILABLE_TOOLS.items()])
        
        # 2. Construct the prompt
        prompt = f"""
        {SYSTEM_PROMPT}
        
        Context: {context}
        Available Tools: {tool_descriptions}
        
        Business Question: {question}
        """

        # 3. Call the Gemini API
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            )
        )

        # Check if the response was blocked or failed
        if not response.text:
            raise ValueError("Gemini returned an empty response. Check API quota or prompt.")

        response_text = response.text
        
        # Safety check: strip markdown backticks if Gemini ignores the JSON config
        if response_text.startswith("```json"):
            response_text = response_text[7:-3]
        elif response_text.startswith("```"):
            response_text = response_text[3:-3]

        # 4. Parse the JSON response into our Pydantic model
        result_json = json.loads(response_text)
        
        # Validate and return the structured object
        return InvestigationResponse(**result_json)
        
    except Exception as e:
        # This prints the EXACT error to your Render logs so we can see it
        print("\n" + "="*50)
        print("AI INVESTIGATION ERROR:")
        print(str(e))
        print(traceback.format_exc())
        print("="*50 + "\n")
        
        # Raise a clean error for the frontend
        raise ValueError(f"AI Investigation failed: {str(e)}")