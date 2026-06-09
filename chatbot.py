"""
Simple Rule-Based Chatbot (CLI)
================================
A beginner-friendly chatbot using if-elif statements.
Topics: greetings, FAQs about Python, general questions, farewells.
"""

def get_response(user_input):
    """Return a bot reply based on the user's message."""
    msg = user_input.lower().strip()

    # ── Greetings ──────────────────────────────────────────────
    if msg in ["hi", "hello", "hey", "howdy", "hlo"]:
        return "Hello! 👋 I'm PyBot. Ask me anything about Python or just chat!"

    elif "good morning" in msg:
        return "Good morning! ☀️ Hope you have a productive coding day!"

    elif "good night" in msg:
        return "Good night! 🌙 Sweet dreams and happy coding tomorrow!"

    elif "how are you" in msg or "how r u" in msg:
        return "I'm just a program, but I'm running perfectly! 😄 How can I help you?"

    elif "what is your name" in msg or "who are you" in msg:
        return "I'm PyBot 🤖 — a simple rule-based chatbot built with Python if-elif logic!"

    # ── Python FAQs ────────────────────────────────────────────
    elif "what is python" in msg:
        return (
            "Python is a high-level, interpreted programming language known for its\n"
            "simple syntax and readability. It's widely used in AI/ML, web dev,\n"
            "automation, data science, and more!"
        )

    elif "who created python" in msg or "who made python" in msg:
        return "Python was created by Guido van Rossum and first released in 1991. 🐍"

    elif "what is a variable" in msg:
        return (
            "A variable is a named container that stores a value.\n"
            "Example:\n"
            "  name = 'Hepsibha'   # string\n"
            "  age  = 20           # integer\n"
            "  gpa  = 9.2          # float"
        )

    elif "what is a list" in msg:
        return (
            "A list is an ordered, mutable collection in Python.\n"
            "Example:\n"
            "  fruits = ['apple', 'mango', 'banana']\n"
            "  print(fruits[0])  # apple"
        )

    elif "what is a function" in msg:
        return (
            "A function is a reusable block of code defined with the 'def' keyword.\n"
            "Example:\n"
            "  def greet(name):\n"
            "      return f'Hello, {name}!'\n"
            "  print(greet('World'))  # Hello, World!"
        )

    elif "what is a loop" in msg or "loops in python" in msg:
        return (
            "Python has two main loops:\n"
            "  • for  — iterate over a sequence\n"
            "  • while — repeat while a condition is True\n\n"
            "Example:\n"
            "  for i in range(3):\n"
            "      print(i)   # 0 1 2"
        )

    elif "what is a dictionary" in msg or "what is dict" in msg:
        return (
            "A dictionary stores key-value pairs.\n"
            "Example:\n"
            "  student = {'name': 'Hepsibha', 'branch': 'AI/ML'}\n"
            "  print(student['name'])  # Hepsibha"
        )

    elif "what is oop" in msg or "object oriented" in msg:
        return (
            "OOP (Object-Oriented Programming) organises code into classes & objects.\n"
            "Key pillars: Encapsulation, Inheritance, Polymorphism, Abstraction.\n"
            "Python supports OOP with the 'class' keyword."
        )

    elif "what is pip" in msg:
        return (
            "pip is Python's package installer.\n"
            "Usage:\n"
            "  pip install requests       # install a package\n"
            "  pip list                   # see installed packages\n"
            "  pip uninstall requests     # remove a package"
        )

    # ── General / Small Talk ───────────────────────────────────
    elif "joke" in msg or "tell me a joke" in msg:
        return "Why do programmers prefer dark mode?\n...Because light attracts bugs! 🐛😄"

    elif "help" in msg:
        return (
            "Sure! You can ask me about:\n"
            "  • Python basics (variables, lists, loops, functions, dicts, OOP, pip)\n"
            "  • Greetings & small talk\n"
            "  • A joke 😄\n"
            "  • Type 'bye' to exit."
        )

    elif "thank" in msg:
        return "You're welcome! Happy to help anytime. 😊"

    elif "sorry" in msg:
        return "No worries at all! What can I help you with?"

    # ── Farewells ──────────────────────────────────────────────
    elif msg in ["bye", "goodbye", "exit", "quit", "see you", "cya"]:
        return "QUIT"   # signal to the main loop to exit

    # ── Fallback ───────────────────────────────────────────────
    else:
        return (
            "Hmm, I didn't understand that. 🤔\n"
            "Try asking about Python topics, or type 'help' to see what I can do!"
        )


def main():
    print("=" * 50)
    print("   Welcome to PyBot 🤖  (Rule-Based Chatbot)")
    print("   Type 'help' for topics | 'bye' to exit")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nPyBot: Goodbye! 👋")
            break

        if not user_input:
            print("PyBot: Please type something!")
            continue

        response = get_response(user_input)

        if response == "QUIT":
            print("PyBot: Goodbye! Keep coding! 👋🐍")
            break

        print(f"PyBot: {response}")


if __name__ == "__main__":
    main()