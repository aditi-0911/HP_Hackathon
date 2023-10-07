from flask import Flask, render_template, redirect, Response

from worksheets.guess_the_time_1 import guess_the_time
from worksheets.match_the_time_words import match_the_time_words
from worksheets.draw_the_time import draw_the_time
from worksheets.write_time_in_numbers import write_time_in_numbers
from worksheets.clock_without_hands_words1 import clock_without_hands_words
from worksheets.match_clock_wordtime import match_clock_wordtime
from worksheets.match_the_time_num import match_the_time_num

app = Flask(__name__)

@app.route('/')
def hello():
    message = "Hello, Flask!"
    return render_template('index.html', message=message)


@app.route('/guess_the_time_worksheet')
def hello1():
    message = "Hello, Flask!"
    #print("hello2 called!!!!!")
    loc = guess_the_time()
    with open(loc, "rb") as f:
        content = f.read()
    response = Response(content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=Time Telling Worksheet.pdf'
    return response
    #return redirect(loc, code=302)
    #return render_template('index.html', message=message)

@app.route('/match_the_time_worksheet')
def hello2():
    message = "Hello, Flask!"
    loc = match_the_time_words()
    with open(loc, "rb") as f:
        content = f.read()
    response = Response(content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=Time Telling Worksheet.pdf'
    return response
    return render_template('index.html', message=message)

@app.route('/draw_the_time_worksheet')
def hello3():
    message = "Hello, Flask!"
    loc = draw_the_time()
    with open(loc, "rb") as f:
        content = f.read()
    response = Response(content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=Time Telling Worksheet.pdf'
    return response
    return render_template('index.html', message=message)

@app.route('/write_time_in_numbers')
def hello4():
    message = "Hello, Flask!"
    loc = write_time_in_numbers()
    with open(loc, "rb") as f:
        content = f.read()
    response = Response(content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=Time Telling Worksheet.pdf'
    return response
    return render_template('index.html', message=message)

@app.route('/clock_without_hands_words')
def hello5():
    message = "Hello, Flask!"
    loc = clock_without_hands_words()
    with open(loc, "rb") as f:
        content = f.read()
    response = Response(content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=Time Telling Worksheet.pdf'
    return response
    return render_template('index.html', message=message)

@app.route('/match_clock_wordtime')
def hello6():
    message = "Hello, Flask!"
    loc = match_clock_wordtime()
    with open(loc, "rb") as f:
        content = f.read()
    response = Response(content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=Time Telling Worksheet.pdf'
    return response
    return render_template('index.html', message=message)

@app.route('/match_the_time_num')
def hello7():
    message = "Hello, Flask!"
    loc = match_the_time_num()
    with open(loc, "rb") as f:
        content = f.read()
    response = Response(content, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'inline; filename=Time Telling Worksheet.pdf'
    return response
    return render_template('index.html', message=message)




if __name__ == '__main__':
    app.run()
