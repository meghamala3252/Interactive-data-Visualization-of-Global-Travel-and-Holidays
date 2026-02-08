import random
from datetime import datetime

def generate_itinerary(destination, days, budget_level, month):
    """
    Generates a mock AI itinerary based on inputs.
    In production, this would query an LLM (OpenAI/Gemini).
    """
    
    # Mock Weather Data
    weather_map = {
        'June': 'Sunny, 25°C', 'July': 'Hot, 30°C', 'August': 'Hot, 29°C',
        'December': 'Cold, 5°C', 'January': 'Snowy, -2°C'
    }
    weather = weather_map.get(month, 'Mild, 20°C')
    
    # Mock Cost
    base_cost = 150 if budget_level == 'Budget' else 400
    total_cost = base_cost * int(days)
    
    # Mock Itinerary Plan
    plan = []
    activities = [
        "Visit the National Museum", "City Walking Tour", "Local Food Tasting",
        "Historical Landmark Visit", "Nature Park Hike", "Night Market Exploration",
        "River Cruise", "Shopping District", "Cultural Performance"
    ]
    
    for day in range(1, int(days) + 1):
        day_plan = {
            "day": day,
            "morning": random.choice(activities),
            "afternoon": random.choice(activities),
            "evening": "Dinner at a local favorite spot"
        }
        plan.append(day_plan)
        
    return {
        "destination": destination,
        "best_travel_month": month,
        "weather_forecast": weather,
        "crowd_level": "High" if month in ['June', 'July', 'August'] else "Moderate",
        "estimated_cost": f"${total_cost} USD",
        "daily_plan": plan
    }
