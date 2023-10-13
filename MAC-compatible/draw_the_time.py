from PIL import Image
from reportlab.lib.pagesizes import letter
import random
from reportlab.pdfgen import canvas
import os


def draw_the_time():
    location = os.getcwd()
    num_clocks=5
    # Open the original image
    
    original_image = Image.open(location + '/diall.png')

    # Define the output PDF file name
    pdf_filename = "draw_the_time.pdf"

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

    image_texts = []
    for i in range(num_clocks):
        image_texts.append(f'{arr1[i]:02}:{arr2[i]:02}')
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
    doc_loc=location + '/draw_the_time.pdf'
    for i in range(num_duplicates):
        duplicate_image_filename = f"image_copy_{i}.png"
        os.remove(duplicate_image_filename)
    return doc_loc

    # Clean up: Delete the duplicate image files
draw_the_time()
