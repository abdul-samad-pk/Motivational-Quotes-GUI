from tkinter import *
from bs4 import BeautifulSoup
import requests

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = '#C9F31D'
QUOTE_BOX_COLOR = '#FFFFFF'
BUTTON_COLOR = '#000000'
TEXT_COLOR = '#333333'
FONT_NAME = "Helvetica"


class MotivationQuotesGUI:
    """
    A GUI application that fetches and displays motivational quotes
    scraped from an online source using requests and BeautifulSoup.
    """

    def __init__(self):
        """
        Initializes the MotivationQuotesGUI with a target URL.
        """
        self.url = 'https://www.quotewis.com/random/motivational-quotes'

    def get_quotes(self):
        """
        Fetches a random motivational quote and its author from the website.

        Returns:
            list[str]: A list with the quote and author.
                       If there's an error, returns a fallback message.
        """
        try:
            response = requests.get(url=self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            quote = soup.find(name='h1', class_='h3 card-title text-dark').text.strip()
            author = soup.find(name='a', class_='text-secondary text-monospace font-italic').text.strip()
            return [quote, author]
        except:
            return ["Error fetching quote. Try again.", ""]

    def gui_tk(self):
        """
        Sets up and runs the Tkinter GUI.
        Displays a canvas with the title, quote text, author, and a button to fetch new quotes.
        """
        window = Tk()
        window.title("Motivational Quotes")
        window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        canvas = Canvas(width=600, height=400, bg=QUOTE_BOX_COLOR, highlightthickness=0)
        canvas.grid(row=0, column=0, columnspan=2, pady=(0, 30))

        # Title text at top
        title_text = canvas.create_text(
            300, 40,
            text="💬 Daily Motivation",
            font=(FONT_NAME, 24, "bold"),
            fill=TEXT_COLOR
        )

        # Quote content text
        quote_text = canvas.create_text(
            300, 180,
            text="Click below to generate a quote.",
            width=500,
            font=(FONT_NAME, 16, "italic"),
            fill=TEXT_COLOR,
            justify="center"
        )

        # Author name text
        author_text = canvas.create_text(
            300, 300,
            text="",
            font=(FONT_NAME, 14, "bold"),
            fill="#888888"
        )

        def quote_replacer():
            """
            Callback to fetch a new quote and update the canvas content.
            """
            quote, author = self.get_quotes()
            canvas.itemconfig(quote_text, text=f'"{quote}"')
            canvas.itemconfig(author_text, text=f"- {author}")

        # Generate button
        generate_button = Button(
            text="✨ Generate Quote",
            command=quote_replacer,
            font=(FONT_NAME, 12, "bold"),
            bg=BUTTON_COLOR,
            fg="white",
            padx=20,
            pady=10,
            borderwidth=0,
            activebackground="grey5",
            activeforeground="white"
        )
        generate_button.grid(row=1, column=0, columnspan=2)

        window.mainloop()


# Run the app
mq_gui = MotivationQuotesGUI()
mq_gui.gui_tk()
