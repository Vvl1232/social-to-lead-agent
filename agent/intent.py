def detect_intent(message: dict) -> str:
    """
    Detect user intent from a LangChain-style message dict.
    message format: {"role": "user", "content": "..."}
    """

    text = message["content"].lower()

    # HIGH INTENT (check first)
    if any(phrase in text for phrase in [
        "i want",
        "sign up",
        "get started",
        "buy",
        "try",
        "pro plan"
    ]):
        return "high_intent"

    # PRODUCT / PRICING INQUIRY
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

    # GREETING
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    return "unknown"