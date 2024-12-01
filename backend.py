from flask import Flask, render_template, send_from_directory, request, make_response
import random
from database import get_count, get_skill
import json

app = Flask(__name__)

LESSON_COUNT = get_count()

@app.route('/')
def home():
    return send_from_directory('static','index.html')

@app.route('/skill')
def skill():
    completed = json.loads(request.cookies.get('completed','[]'))
    random_id = random.randrange(1,LESSON_COUNT+1,1)
    if len(completed) == LESSON_COUNT:
        return render_template(
            'skill.html',
            skill_title='ВЫ ПРОШЛИ ИГРУ',
            skill_description='теперь вы умеете всё на свете, поздравляем!',
            skill_video_id='dQw4w9WgXcQ'
            )
    while (random_id in completed):
        random_id = random.randrange(1,LESSON_COUNT+1,1)
    lesson = get_skill(random_id)
    completed.append(random_id)
    response = make_response(render_template(
        'skill.html',  # Указываем шаблон
        skill_title=lesson['skillName'],  # Название навыка
        skill_description=lesson['skillDesc'],  # Описание навыка
        skill_video_id=lesson['skillUrl']  # ID видео на YouTube
    ))
    response.set_cookie('completed',json.dumps(completed))
    return response


