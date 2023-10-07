from PIL import Image
from reportlab.lib.pagesizes import letter
import random
from reportlab.pdfgen import canvas
import os

def clock_without_hands_words():
    location = os.getcwd()
    num_clocks=5
    # Open the original image
    original_image_path = "path_to_original_image.png"  # Replace with your image path
    original_image = Image.open('/Users/shreymaheshwari/Desktop/untitled folder/diall.png')

    # Define the output PDF file name
    pdf_filename = "clock_without_hands_words.pdf"

    # Create a PDF canvas
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Define the number of duplicate images and text you want to create
    num_duplicates = 5
    def hour(array):
        while(len(array)!=num_clocks):
            y = random.randrange(1,13)
            array.add(y)
        return list(array)

    def minute(array):
        while(len(array)!=num_clocks):
            y = random.randrange(0,60,5)
            array.add(y)
        return list(array)

    arr1 = hour(set([]))
    arr2 = minute(set([]))



    def time_to_words(hour,minute):
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

    image_texts = []
    for i in range(num_clocks):
        image_texts.append(time_to_words(arr1[i],arr2[i]))
    text = image_texts

    # Define the position to start drawing images and text
    x_image = 20
    x_text = 400
    y = 500

    # Loop to create and add duplicate images and text to the PDF
    for i in range(num_duplicates):
        # Create a copy of the original image
        duplicate_image = original_image.copy()

        # Define the filename for the duplicate image
        duplicate_image_filename = f"image_copy_{i}.png"

        # Save the duplicate image
        duplicate_image.save(duplicate_image_filename)

        # Draw the image on the PDF
        c.drawImage(duplicate_image_filename, x_image, 100+y, width=150, height=150)

        # Draw text on the right side of the image
        c.drawString(x_text, y+170, text[i])

        # Move to the next position for the next image and text
        y -= 200

    # Save the PDF file
    c.save()
    doc_loc = location + '/clock_without_hands_words.pdf'
    return doc_loc

    # Clean up: Delete the duplicate image files
    for i in range(num_duplicates):
        duplicate_image_filename = f"image_copy_{i}.png"
        os.remove(duplicate_image_filename)
