def detect_intent(query):
    query = query.lower()

    if "crop" in query:
        return "crop_recommendation"
    elif "water" in query or "irrigation" in query:
        return "irrigation"
    elif "disease" in query:
        return "disease"
    else:
        return "general"
