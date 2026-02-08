import os
import pandas as pd
import random
import re

# Load Data Once
DATA_PATH = os.path.join(os.getcwd(), 'data', 'tourism_data.csv')
df = None
try:
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
except Exception as e:
    print(f"Error loading chatbot data: {e}")

def query_dataframe(query):
    """
    Simple logic to extract answers from the loaded CSV data.
    """
    if df is None:
        return None
        
    q = query.lower()
    
    # 1. Check for Country specific stats
    # Regex to find country name in query
    countries = df['country'].unique()
    found_country = None
    for country in countries:
        if country.lower() in q:
            found_country = country
            break
            
    if found_country:
        country_data = df[df['country'] == found_country]
        
        if "spending" in q:
            avg_spend = country_data['spending_usd'].mean()
            return f"The average tourist spending in {found_country} is approximately ${avg_spend:,.2f} USD."
        
        if "arrivals" in q or "visitors" in q:
            total_arrivals = country_data['arrivals'].sum()
            return f"Total recorded arrivals for {found_country} are {total_arrivals:,} visitors."
            
        if "region" in q:
            region = country_data['region'].iloc[0]
            return f"{found_country} is located in the {region} region."

    return None

def query_llm(query):
    """
    Queries OpenAI or Google Gemini if keys are available.
    """
    # 1. Try OpenAI
    openai_key = os.environ.get('OPENAI_API_KEY')
    if openai_key:
        try:
            import openai
            openai.api_key = openai_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful Tourism AI assistant. Answer questions about travel, tourism trends, and culture concisely."},
                    {"role": "user", "content": query}
                ]
            )
            return response.choices[0].message.content
        except ImportError:
            print("OpenAI module not found/working.")
        except Exception as e:
            print(f"OpenAI Error: {e}")
            
    # 2. Try Google Gemini
    gemini_key = os.environ.get('GEMINI_API_KEY')
    if gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(f"You are a Tourism AI. {query}")
            return response.text
        except ImportError:
            print("Google GenerativeAI module not found/working.")
        except Exception as e:
            print(f"Gemini Error: {e}")
            
    return None

def get_chat_response(message):
    """
    Hybrid Chatbot: Data -> LLM -> Knowledge Base
    """
    msg = message.lower()
    
    # 1. Try Data Query (Exact stats)
    data_ans = query_dataframe(msg)
    if data_ans:
        return data_ans
        
    # 2. Try LLM (General Knowledge)
    llm_ans = query_llm(message)
    if llm_ans:
        return llm_ans
        
    # 3. Fallback Rule-Based Knowledge Base
    rules = {
        "hello": "Hello! I am your AI Tourism Assistant. I can help you with stats from our database or general travel questions.",
        "hi": "Hi there! Ready to explore the world?",
        "trend": "Based on global data, tourism peaks significantly during June-August (Summer) and December (Holidays).",
        "recommend": "I recommend checking the 'Global Tourism Overview' dashboard. For a specific trip, try our Itinerary Planner!",
        "visa": "Visa requirements vary by country. It's best to check the official government website of your destination.",
        "weather": "I can check historical weather trends if you specify a country and month.",
        "best time": "Generally, the shoulder seasons (Spring and Autumn) offer the best balance of good weather and fewer crowds.",
        "budget": "For budget travel, consider destinations in Southeast Asia or Eastern Europe. For luxury, Western Europe and North America are popular.",
        "help": "I can answer questions like: 'Spending in France', 'Arrivals in USA', 'Travel tips for Japan', etc."
    }
    
    for key, response in rules.items():
        if key in msg:
            return response
            
    # 4. Generic Fallback
    return "I don't have that specific information yet. To get the best answers, please ensure your OpenAI or Gemini API key is configured in the .env file, or ask me about specific country statistics present in the database."

