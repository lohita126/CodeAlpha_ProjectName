# faq_bot.py

# A simple FAQ dictionary
FAQS = {
    "what are your hours": "We are open from 9am to 6pm, Monday to Friday.",
    "how can i contact support": "You can contact support via email: support@example.com.",
    "what is your refund policy": "Our refund policy allows returns within 30 days of purchase with receipt.",
    "where are you located": "We are located at 123, Main Street, Cityville.",
}

def find_best_faq_answer(user_input: str) -> str:
    """
    Simple keyword matching: check if any FAQ key is in the user_input.
    """
    user_input_lower = user_input.lower()
    for faq_question, faq_answer in FAQS.items():
        if faq_question in user_input_lower:
            return faq_answer
    return None

def main():
    print("FAQ Chatbot — type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            print("Chatbot: Goodbye!")
            break
        
        answer = find_best_faq_answer(user_input)
        if answer:
            print("Chatbot:", answer)
        else:
            print("Chatbot: Sorry, I don't understand. Can you rephrase or ask something else?")
            
if __name__ == "__main__":
    main()
