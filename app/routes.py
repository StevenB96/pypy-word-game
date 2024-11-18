# routes.py

from flask import Flask, render_template
from classes.WordGame import WordGame

app = Flask(__name__)

@app.route('/')
def index():
    game = WordGame("hello")  # Create an instance of WordGame
    word_length = game.get_word_length()
    palindrome_check = game.is_palindrome()
    
    return render_template('index.html', word="hello", length=word_length, is_palindrome=palindrome_check)