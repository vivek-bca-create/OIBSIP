import datetime
import os
import sys
import webbrowser
import pyttsx3

# Initialize the localization text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Function to make the system speak the given text feedback loop."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def greet_user():
    """Greets the user based on the current time of the day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your desktop assistant. How can I help you today?")


def process_command(command):
    """Parses and executes the user command using standard control flows."""
    command = command.lower().strip()

    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        # Added voice feedback for time execution
        speak(f"The current time is {current_time}.")

    elif "open google" in command:
        # Added voice feedback before opening the website
        speak("Opening Google Chrome right now.")
        webbrowser.open("https://google.com")

    elif "search google" in command:
        search_query = command.replace("search google for", "").replace(
            "search google", ""
        )
        search_query = search_query.strip()
        if search_query:
            speak(f"Searching Google for {search_query}.")
            webbrowser.open(f"https://google.com/search?q={search_query}")
        else:
            speak("What would you like me to search for?")

    elif "open youtube" in command:
        # Added voice feedback for youtube navigation
        speak("Opening YouTube for you.")
        webbrowser.open("https://youtube.com")

    elif "exit" in command or "quit" in command or "stop" in command:
        speak("Goodbye! Have a great day ahead.")
        return False

    else:
        speak("I am sorry, I can only search Google, open websites, or tell the time.")

    return True


def main():
    """Main execution loop for the desktop assistant."""
    greet_user()
    is_running = True

    while is_running:
        user_input = input("\nEnter your command (or type 'exit'): ")
        if user_input.strip() == "":
            continue
        is_running = process_command(user_input)


if __name__ == "__main__":
    main()
