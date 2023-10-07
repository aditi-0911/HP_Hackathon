from PIL import Image, ImageDraw
import random
import PIL
import math
import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.pdfgen import canvas
from PIL import Image as PILImage
from os import walk

def match_the_time_num():
    location = os.getcwd()
    num_clocks=5


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


    # Function to generate a random clock dial
    def generate_clock_dial(hour, minute, second, filename="clock_dial.png"):
        # Create a blank white canvas
        width, height = 400, 400
        # dial = Image.new("RGB", (width, height), "white")

        dial = PIL.Image.open(location + "/diall.png")
        draw = ImageDraw.Draw(dial)    
        center_x, center_y = width // 2, height // 2


        # Draw the clock circle
        clock_radius = min(width, height) // 2 - 10
        # draw.ellipse((center_x - clock_radius, center_y - clock_radius, center_x + clock_radius, center_y + clock_radius), outline="black", width=2)

        # Draw hour markers
        # for hour in range(1, 13):
        #     angle = math.radians(360 / 12 * hour - 90)
        #     marker_x = center_x + clock_radius * 0.9 * math.cos(angle)
        #     marker_y = center_y + clock_radius * 0.9 * math.sin(angle)
        #     draw.line((center_x, center_y, marker_x, marker_y), fill="black", width=2)

        # Draw clock hands (hour, minute, second)
        hour_angle = math.radians(360 / 12 * hour - 90)
        minute_angle = math.radians(360 / 60 * minute - 90)
        second_angle = math.radians(360 / 60 * second - 90)

        # Hour hand
        hour_hand_length = clock_radius * 0.5
        hour_x = center_x + hour_hand_length * math.cos(math.sin(math.radians(hour * 30 + 0.5 * minute)))
        hour_y = center_y + hour_hand_length * math.sin(math.sin(math.radians(hour * 30 + 0.5 * minute)))
        #hour_x = center_x + hour_hand_length * math.cos(hour_angle)
        #hour_y = center_y + hour_hand_length * math.sin(hour_angle)
        draw.line((center_x, center_y, hour_x, hour_y), fill="black", width=6)

        # Minute hand
        minute_hand_length = clock_radius * 0.7
        minute_x = center_x + minute_hand_length * math.cos(minute_angle)
        minute_y = center_y + minute_hand_length * math.sin(minute_angle)
        draw.line((center_x, center_y, minute_x, minute_y), fill="blue", width=4)

        # # Second hand
        # second_hand_length = clock_radius * 0.8
        # second_x = center_x + second_hand_length * math.cos(second_angle)
        # second_y = center_y + second_hand_length * math.sin(second_angle)
        # draw.line((center_x, center_y, second_x, second_y), fill="red", width=2)

        return dial

    # Create a directory to store the generated clock dials
    output_directory = location + '/clock_dials'
    os.makedirs(output_directory, exist_ok=True)


    arr1 = hour(set([]))
    arr2 = minute(set([]))

    # Generate and save multiple random clock dials as PNG images
    #num_clocks = 4  # Number of clock dials to generate
    for i in range(num_clocks):
        clock_dial = generate_clock_dial(arr1[i],arr2[i],0)
        filename = os.path.join(output_directory, f"clock_{i + 1}.png")
        clock_dial.save(filename)

    print(f"{num_clocks} clock dials saved in {output_directory}")




    # Folder containing the images
    image_folder = output_directory  # Replace with the path to your image folder

    # List of image files in the folder
    image_files = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith((".png", ".jpg", ".jpeg"))]

    image_texts = []
    # Corresponding text for each image
    for i in range(num_clocks):
        image_texts.append(f'{arr1[i]:02}:{arr2[i]:02}')
      # Add your text here
    random.shuffle(image_texts)

    # Create a PDF document
    pdf_filename = "match_the_time_num.pdf"
    pdf = canvas.Canvas(pdf_filename, pagesize=letter)

    # Set the left margin for the images
    left_margin = 50

    # Set the initial y-coordinate for the images and text
    y_coordinate = 750  # Adjust as needed

    # Set the font for the text
    text_font = "Helvetica"
    text_font_size = 12

    # Insert each image and its corresponding text on the left and right sides of the page
    for image_file, text in zip(image_files, image_texts):
        # Open the image using Pillow
        img = PIL.Image.open(image_file)

        # Calculate the aspect ratio to maintain the image's proportions
        width, height = img.size
        aspect_ratio = height / float(width)
        new_width = 100  # Adjust the width as needed
        new_height = int(new_width * aspect_ratio)

        # Insert the image on the left side of the page
        pdf.drawImage(image_file, left_margin, y_coordinate - new_height, width=new_width, height=new_height)

        # Draw the text on the right side of the page
        pdf.setFont(text_font, text_font_size)
        pdf.drawString(left_margin + new_width + 300, y_coordinate - (new_height-40), text)

        # Adjust the y-coordinate for the next image and text
        y_coordinate -= (new_height + 10)  # 10 is the spacing between images and text
        img.close()
       
    # Save the PDF file

    pdf.save()
    doc_loc = location + '/match_the_time_num.pdf'
    for i in range(num_clocks):
        to_delete = location + f'\clock_dials\clock_{i+1}.png'
        os.remove(to_delete)
    os.rmdir(location + '\clock_dials')    

    return doc_loc

match_the_time_num()
    # print(f"PDF with images and text saved as {pdf_filename}")