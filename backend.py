from flask import Flask, render_template, send_from_directory, request
import random
from database import get_count, get_skill

app = Flask(__name__)

LESSON_COUNT = get_count()

@app.route('/')
def home():
    return send_from_directory('static','index.html')

@app.route('/skill')
def skill():
    completed = list(request.cookies.get('completed',[]))
    random_id = random.randrange(1,LESSON_COUNT+1,1)
    while (random_id in completed):
        random_id = random.randrange(1,LESSON_COUNT+1,1)
    lesson = get_skill(random_id)
    completed.append(random_id)
    response = render_template('lesson.html', lesson=lesson)
    response.set_cookie('completed',f'{completed}')
    return response


