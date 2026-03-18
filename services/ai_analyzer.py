from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def analyze_data(sector: str, data: str):
    try:
        prompt = f"""
        Analyze the {sector} sector in India.

        Data:
        {data}

        Generate a structured markdown report with:
        ## Overview
        ## Current Trends
        ## Trade Opportunities
        ## Risks
        ## Conclusion
        """

        # ✅ ONLY allow known working TEXT models
        preferred_models = [
            "llama-3.1-8b-instant",
            "llama-3.1-70b-versatile",
            "gemma2-9b-it"
        ]

        for model_name in preferred_models:
            try:
                response = client.chat.completions.create(
                    model=model_name,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                content = response.choices[0].message.content

                # ✅ Ensure valid text output
                if content and len(content) > 50:
                    return content

            except Exception:
                continue

        return "Error: No valid text model available"

    except Exception as e:
        return f"Error: {str(e)}"