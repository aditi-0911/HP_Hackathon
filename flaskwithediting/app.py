from flask import Flask, request, render_template, redirect, url_for
from flask import Flask, render_template, redirect, Response, send_file
import subprocess

app = Flask(__name__)

# Route to display the input form
@app.route('/')
def index():
    return render_template('input_form.html')

# Route to receive form data and redirect to the greeting page
@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form.get('name')
    age = request.form.get('age')
    return redirect(url_for('greet', name=name, age=age))

# Route for the greeting page with options
@app.route('/greet/<name>/<age>')
def greet(name, age):
    return render_template('greeting_page.html', name=name, age=age)

@app.route('/generate_pdf/<program_name>')
def generate_pdf(program_name):
    # Execute the corresponding Python program using subprocess
    try:
        if program_name == "clock_without_hands_words1":
            subprocess.run(['python', f'{program_name}.py'], check=True)
            return send_file(f'{program_name}.pdf', as_attachment=True)
        elif program_name == "guess_the_time_1":
            subprocess.run(['python', f'{program_name}.py'], check=True)
            return send_file(f'{program_name}.pdf', as_attachment=True)
        elif program_name == "match_clock_wordtime":
            subprocess.run(['python', f'{program_name}.py'], check=True)
            return send_file(f'{program_name}.pdf', as_attachment=True)       
        elif program_name == "match_the_time_num":
            subprocess.run(['python', f'{program_name}.py'], check=True)
            return send_file(f'{program_name}.pdf', as_attachment=True)       
        elif program_name == "match_the_time_words":
            subprocess.run(['python', f'{program_name}.py'], check=True)
            return send_file(f'{program_name}.pdf', as_attachment=True)       
        elif program_name == "write_time_in_numbers":
            subprocess.run(['python', f'{program_name}.py'], check=True)
            return send_file(f'{program_name}.pdf', as_attachment=True)       
        elif program_name == "draw_the_time":
            subprocess.run(['python', f'{program_name}.py'], check=True)
            return send_file(f'{program_name}.pdf', as_attachment=True)            
        # Return the generated PDF file
    except Exception as e:
        return str(e)

# Add more routes for handling options on the greeting page

if __name__ == '__main__':
    app.run(debug=True)
