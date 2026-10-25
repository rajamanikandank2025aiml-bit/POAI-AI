# Query Execution System in Artificial Intelligence

import datetime
import math

def execute_query(query):
    query = query.lower().strip()

    # Greeting queries
    if query in ["hello", "hi", "hey"]:
        return "Hello! Welcome to the AI Query System."

    # Identity queries
    elif "your name" in query:
        return "I am an Artificial Intelligence Query System."

    # Date query
    elif "date" in query:
        return "Today's date is " + str(datetime.date.today())

    # Time query
    elif "time" in query:
        return "Current time is " + str(
            datetime.datetime.now().strftime("%H:%M:%S")
        )

    # Mathematical queries
    elif query.startswith("add"):
        try:
            numbers = list(map(float, query.split()[1:]))
            return "Sum = " + str(sum(numbers))
        except ValueError:
            return "Enter numbers after add. Example: add 10 20"

    elif query.startswith("multiply"):
        try:
            numbers = list(map(float, query.split()[1:]))
            result = math.prod(numbers)
            return "Product = " + str(result)
        except ValueError:
            return "Enter numbers after multiply."

    elif query.startswith("square"):
        try:
            number = float(query.split()[1])
            return "Square = " + str(number ** 2)
        except (ValueError, IndexError):
            return "Enter a number. Example: square 5"

    # AI concept queries
    elif "artificial intelligence" in query:
        return (
            "Artificial Intelligence is a branch of computer "
            "science that enables machines to perform tasks "
            "requiring human-like intelligence."
        )

    elif "machine learning" in query:
        return (
            "Machine Learning is a branch of AI that enables "
            "computers to learn patterns from data."
        )

    elif "deep learning" in query:
        return (
            "Deep Learning uses multi-layer neural networks "
            "to learn complex patterns."
        )

    elif "query execution" in query:
        return (
            "Query execution is the process of interpreting "
            "a query, processing it, and returning a result."
        )

    elif "python" in query:
        return (
            "Python is a high-level programming language "
            "used in AI, automation, and data science."
        )

    # General knowledge queries
    elif "capital of india" in query:
        return "The capital of India is New Delhi."

    elif "largest planet" in query:
        return "Jupiter is the largest planet in our solar system."

    elif "water formula" in query:
        return "The chemical formula of water is H2O."

    # Exit query
    elif query in ["exit", "quit", "bye"]:
        return "Goodbye! Thank you for using the AI system."

    # Unknown query
    else:
        return (
            "Sorry, I do not understand that query. "
            "Please try another question."
        )


def main():
    print("=" * 50)
    print("       AI QUERY EXECUTION SYSTEM")
    print("=" * 50)
    print("Ask a question or enter a command.")
    print("Commands: add, multiply, square, date, time")
    print("Type 'exit' to stop the program.")
    print("-" * 50)

    while True:
        query = input("\nEnter your query: ")

        if query.lower().strip() in ["exit", "quit", "bye"]:
            print("AI:", execute_query(query))
            break

        result = execute_query(query)
        print("AI:", result)


if __name__ == "__main__":
    main()
