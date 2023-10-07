# HP_Hackathon

Time Telling Worksheet Generator

## Table of Contents

1. [Overview](#overview)
2. [Purpose](#Purpose)
3. [Key Features](#Key-Features)
4. [File Structure](#file-structure)

## Overview

This project is a web-based tool for generating time-telling worksheets dynamically. It combines Python code for worksheet generation with HTML templates using Flask, allowing users to create customized time-telling practice sheets effortlessly.

## Purpose

The primary purpose of this project is to provide teachers, parents, and students with a versatile and convenient tool for practicing time-telling skills. By generating worksheets on the fly, it eliminates the need for manual worksheet creation, saving valuable time for educators and learners.

## Key Features

- **Dynamic Worksheet Generation**: With the power of Python and Flask, this tool generates time-telling worksheets with varying levels of complexity and different sets of problems instantly.

- **Customization**: Users can tailor worksheets to meet their specific needs by selecting the type of time-telling problems, the number of questions, and other parameters.

- **Interactive Interface**: The web-based interface makes it user-friendly and accessible to individuals of all ages. Worksheets can be generated with just a few clicks.

- **Real-time Timer**: For added educational value, a timer is integrated into the worksheets to help learners track the time spent on each problem.

- **User Guide**: Detailed instructions and tips are available in the user guide to ensure that users can maximize the benefits of this tool.

By combining Python's flexibility with Flask's web capabilities, this project aims to simplify time-telling practice while providing an engaging and effective learning experience.

Feel free to explore the repository to learn more about how to use this tool and its underlying code.


## File Structure

Here's an overview of the main files and directories in this repository:

- `templates/`: This directory houses the HTML templates used for this project's web-based user interface. These templates define the structure and layout of the generated webpages. 
    - `index.html`: This is the main HTML template that serves as the entry point for the web application. It is responsible for rendering the user interface and allowing users to interact with the time-telling worksheet generator.
    
- `worksheets/`: This directory houses the python codes used for generating different worksheets.
    - `clock_without_hands_words1.py`:  Generates worksheets where clock hands are omitted, and students must draw the hands of clock given time in words.
    - `write_time_in_numbers.py`: Generates worksheets where students write the time using numerical digits.
    - `draw_the_time.py`: Generates worksheets where students draw clock hands to represent given times.
    - `guess_the_time_1.py`: Generates worksheets where students must guess the time based on visual cues.
    - `match_clock_wordtime.py`: Generates worksheets for matching analog clocks with their corresponding time in words.
    - `match_the_time_num.py`:	Generates worksheets for matching analog clocks with their corresponding numerical times.
    - `match_the_time_words.py`: Generates worksheets for matching numerical times with their corresponding time in words.

- `README.md`: You're currently reading this file. It provides an overview of the project.

- `app.py`: This file contains the Flask code that serves as the core of our web application. It handles routing, rendering HTML templates, and generating time-telling worksheets based on user inputs.

- `diall.png`:This file contains the image of clock without hands used for generating clocks with hands.


Feel free to explore each directory and file for more details about the project's structure and code.



```bash
# Clone the repository
git clone https://github.com/yourusername/your-repo.git

# Change directory to the project folder
cd your-repo

# Install dependencies (if applicable)
pip install -r requirements.txt
