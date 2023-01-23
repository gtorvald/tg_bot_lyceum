import pytz
import datetime


def _get_time_from_string(time: str) -> datetime.time:
    return datetime.datetime.strptime(time, '%H:%M').time()

def get_current_lesson(data: dict) -> str:
    tz_ekb = pytz.timezone('Asia/Yekaterinburg')
    now = datetime.datetime.now(tz_ekb)
    now_weekday = datetime.datetime.now(tz_ekb).weekday()
    # сдвиг уроков в понедельник
    if now_weekday == 0:
        now += datetime.timedelta(minutes=10)
    now_time = now.time()
        
    lessons = data['lessons']
    times = data['times']

    if len(lessons) <= now_weekday or lessons[now_weekday] == []:
        return 'Сегодня нет уроков'
    if _get_time_from_string(times[0]['begin']) > now_time:
        return 'Уроки еще не начались'
    if _get_time_from_string(times[len(times) - 1]['end']) < now_time:
        return 'Уроки уже закончились'

    current_lesson_index = None
    for i in range(len(times)):
        begin = _get_time_from_string(times[i]['begin'])
        end = _get_time_from_string(times[i]['end'])
        if now_time > begin and now_time < end:
            current_lesson_index = i
            break
    
    if (
        current_lesson_index == None or
        len(lessons[now_weekday]) <= current_lesson_index
    ):
        return "Сейчас нет урока"

    return (
        f'Сейчас {times[current_lesson_index]["name"].lower()}: '
        f'{lessons[now_weekday][current_lesson_index]["name"].lower()} в кабинете '
        f'{lessons[now_weekday][current_lesson_index]["office"].lower()}'
    )
