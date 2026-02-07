import random

def agent_decision(intent):
    soil_moisture = random.randint(20, 80)
    temperature = random.randint(20, 40)

    if intent == "irrigation":
        if soil_moisture < 40:
            return "🚿 Soil moisture is low. Irrigation is recommended."
        else:
            return "✅ Soil moisture is sufficient."

    return "🤖 Agent is monitoring conditions."
