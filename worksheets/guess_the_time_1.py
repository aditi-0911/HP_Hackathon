import webbrowser
import math
import os
import PIL
from PIL import Image, ImageDraw
import random
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Image as RLImage, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import subprocess




def guess_the_time():
    styles = getSampleStyleSheet()
    location = os.getcwd()
    num_clocks = 6

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
    output_directory = location + "/dials"
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



    # Function to list image files in a folder
    def list_image_files(folder_path):
        image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp"}
        image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(tuple(image_extensions))]
        return image_files

    # Create a PDF document with landscape orientation
    pdf_filename = "guess_the_time.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=landscape(letter))

    # Create a story to add elements to the PDF
    story = []
    os.chdir(location)
    # Folder path containing images
    image_folder = output_directory

    # List image files in the folder
    image_files = list_image_files(image_folder)

    # Define the number of images per page
    images_per_page = 6
    current_page_images = []

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        description = " "  # Replace with your image description

        # Open the image and resize if necessary
        img = Image.open(image_path)
        max_width = 100  # Adjust the maximum width as needed
        if img.width > max_width:
            img.thumbnail((max_width, max_width), Image.ANTIALIAS)

        # Create a ReportLab image element
        rl_img = RLImage(image_path, width=img.width, height=img.height)

        # Create a paragraph for the image description
        description_paragraph = Paragraph(description, getSampleStyleSheet()['Normal'])

        # Add the image and description to the current page
        current_page_images.extend([rl_img, description_paragraph])

        # If we have collected 6 images, create a table and add it to the story
        if len(current_page_images) == images_per_page * 2:
            x=[current_page_images[i] for i in range(0,3*2,2)]
            y=[current_page_images[i] for i in range(1,3*2,2)]
            z=[current_page_images[i] for i in range(images_per_page,6*2,2)]
            w=[current_page_images[i] for i in range(images_per_page+1,6*2,2)]
            data = [x,y,z,w]
            table = Table(data, colWidths=[300, 300], rowHeights=100)

            table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ]))

            story.append(table)
            story.append(Spacer(1, 20))
            current_page_images = []

    # If there are remaining images, create the last table and add it to the story
    if current_page_images:
       # s=[current_page_images[i] for i in range(images_per_page+5,9*2,2)]
       # t=[current_page_images[i] for i in range(images_per_page+6,9*2,2)]
        #data = [s,t]
        data = [current_page_images[i:i+2] for i in range(0, len(current_page_images), 2)]
        table = Table(data, colWidths=[300, 300], rowHeights=100)

        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('INNERGRID', (0, 0), (-1, -1), 1.5, colors.black),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ]))

        story.append(table)
        story.append(Spacer(1, 20))

    # Build the PDF document
    doc.build(story)

    doc_loc = location + '/guess_the_time.pdf'
    #subprocess.Popen([doc_loc],shell=True)
    webbrowser.open_new(doc_loc)
    return doc_loc

        





