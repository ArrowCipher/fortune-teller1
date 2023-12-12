import random

print("Welcome to the Fortune Teller Game!")
print("Ask a question about your future, and I will reveal your fortune.")

questions = [
    "What is your most burning question?",
    "Think of a question about your future:",
    "Ask a question that's been on your mind:"
]

question = input(random.choice(questions) + " ")

fortunes = [
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes, definitely.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Don't count on it.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

print("\nThinking...\n")
print("Your fortune: " + random.choice(fortunes))
