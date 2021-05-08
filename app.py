from os import name
import random
from flask import Flask, render_template
from flask.globals import request


app = Flask(__name__)
lines = []
words = []


@app.route('/', methods=['POST','GET'])
def index():
    global words
    if request.method == 'POST':
        if request.form['btn'] == 'Да':
            generate_new_file()
            return render_template('index.html', words=words)
        elif request.form['btn'] == 'Нет':
            words = generate_words()
            return render_template('index.html', words=words)
    else:
        words = generate_words()
        return render_template('index.html', words=words)


def generate_words():
    global lines
    return_words = []
    with open('words.txt', 'r', encoding = 'utf-8') as f:
        new_lines = [] 
        num = int(f.readline())
        lines_list = []
        for i in range(20):
            lines_list.append(random.randrange(1, num))
        lines_list.sort()
        index = 1
        while index != num:
            if index in lines_list:
                return_words.append(f.readline())
            else:
                new_lines.append(f.readline())
            index+=1
        lines = new_lines
    return return_words


def generate_new_file():
    with open('words.txt', 'w', encoding = 'utf-8') as f:
        f.write(str(len(lines)) + '\n')    
        for i in lines:
            f.write(i)


if __name__ == "__main__":
    app.run(debug=True)