from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import datetime
import random
import os

def match_the_time_words():
    # Function to convert time to words
    location = os.getcwd()
    def time_to_words(time):
        hour, minute = time.hour, time.minute
        hour_words = ["Midnight", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                      "Eleven", "Noon"]
        minute_words = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                        "Nineteen", "Twenty", "Twenty-One", "Twenty-Two", "Twenty-Three", "Twenty-Four", "Twenty-Five",
                        "Twenty-Six", "Twenty-Seven", "Twenty-Eight", "Twenty-Nine", "Half"]

        if minute == 0:
            return f"{hour_words[hour]} o'clock"
        elif minute == 30:
            return f"Half past {hour_words[hour]}"
        elif minute < 30:
            if minute == 15:
                return f"Quarter past {hour_words[hour]}"
            elif minute == 1:
                return f"{minute_words[minute]} minute past {hour_words[hour]}"
            else:
                return f"{minute_words[minute]} minutes past {hour_words[hour]}"
        else:
            if minute == 45:
                return f"Quarter to {hour_words[(hour+1)%12]}"
            elif minute == 59:
                return f"{minute_words[60-minute]} minute to {hour_words[(hour+1)%12]}"
            else:
                return f"{minute_words[60-minute]} minutes to {hour_words[(hour+1)%12]}"

    # Create a PDF document
    doc = SimpleDocTemplate("match_the_time_words.pdf", pagesize=letter)

    # Create a list of flowables for the PDF content
    elements = []

    # Generate times
    times = [datetime.time(hour, minute) for hour in range(1, 13) for minute in [0, 15, 30, 45]]

    # Shuffle the list of times

    # Create a list of time_in_numbers
    time_in_numbers_list = [time.strftime("%I:%M %p") for time in times]

    random.shuffle(times)

    # Iterate through shuffled times and corresponding time_in_numbers
    for time, time_in_numbers in zip(times, time_in_numbers_list):
        time_in_words = time_to_words(time)
        
        # Create a paragraph for the time in words (left side)
        left_style = ParagraphStyle(name='LeftStyle')
        left_paragraph = Paragraph(time_in_words, left_style)
        elements.append(left_paragraph)
        
        # Create a paragraph for the time_in_numbers (right side)
        right_style = ParagraphStyle(name='RightStyle', alignment=2)  # Right align
        right_paragraph = Paragraph(time_in_numbers, right_style)
        elements.append(right_paragraph)
        
        # Add spacing between time entries
        elements.append(Spacer(1, 20))

    # Build the PDF document
    doc.build(elements)
    doc_loc = location + '/match_the_time_words.pdf'
    #subprocess.Popen([doc_loc],shell=True)
    #webbrowser.open_new(doc_loc)
    return doc_loc
    #print("Worksheet generated successfully.")

