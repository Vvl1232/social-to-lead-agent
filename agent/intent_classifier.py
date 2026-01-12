def detect_intent(user_input: str) -> str:
    text = user_input.lower()

    #HIGH INTENT FIRST
    if any(phrase in text for phrase in [
        "i want",
        "sign up",
        "get started",
        "buy",
        "try",
        "pro plan"
    ]):
        return "high_intent"

    #PRODUCT INQUIRY
    if any(word in text for word in [
        "price",
        "pricing",
        "plan",
        "plans",
        "feature",
        "features",
        "basic",
        "pro"
    ]):
        return "product_inquiry"

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    return "unknown"