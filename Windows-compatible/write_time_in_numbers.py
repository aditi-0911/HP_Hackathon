from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
import datetime
import os 

def write_time_in_numbers():
    location = os.getcwd()
    # Function to convert time to words
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
    doc = SimpleDocTemplate("write_time_in_numbers.pdf", pagesize=letter)

    # Create a list of flowables for the PDF content
    elements = []


    title_style = getSampleStyleSheet()['Title']
    title = Paragraph("Write Time In Numbers", title_style)
    elements.append(title)
    elements.append(Spacer(1, 24))
    # Generate times and create spaces for students to write
    for hour in range(1, 13):
        for minute in [0, 15, 30, 45]:
            time = datetime.time(hour, minute)
            time_in_words = time_to_words(time)
            
            # Create a paragraph for the time in words (left side)
            left_style = ParagraphStyle(name='LeftStyle', alignment=TA_LEFT)
            left_paragraph = Paragraph(time_in_words, left_style)
            elements.append(left_paragraph)
            
            # Add a space for students to write the time in numbers (right side)
            right_style = ParagraphStyle(name='RightStyle', alignment=TA_RIGHT)
            right_paragraph = Paragraph("", right_style)
            elements.append(right_paragraph)
            
            # Add spacing between time entries
            elements.append(Spacer(1, 12))

    # Build the PDF document
    doc.build(elements)
    doc_loc=location + '/write_time_in_numbers.pdf'
    return doc_loc

write_time_in_numbers()
