def generate_story_script(dashboard_data, insights):
    """
    Generates a narrative script for the Story Mode.
    """
    title = dashboard_data.get('title', 'Tourism Dashboard')
    
    script = [
        {
            "title": f"Welcome to {title}",
            "text": f"Welcome to the interactive tour of {title}. Let's explore the key trends and insights discovered in this data.",
            "focus_element": "header"
        },
        {
            "title": "Key Trends",
            "text": "As we observe the main chart, we can see significant fluctuations in tourist arrivals over the selected period.",
            "focus_element": "chart_1"
        }
    ]
    
    # Add insights to script
    for insight in insights:
        script.append({
            "title": "Insight",
            "text": insight,
            "focus_element": "general"
        })
        
    script.append({
        "title": "Conclusion",
        "text": "This concludes our brief tour. Feel free to explore the dashboard further.",
        "focus_element": "footer"
    })
    
    return script
