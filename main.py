from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

@app.get('/')
async def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:
                filtered_students.append(student)
        return filtered_students
    return data

@app.get('/stats')
async def get_stats():
    stats = {}

    for student in data:
        if student['pref'] in stats:
            stats[student['pref']] += 1
        else:
            stats[student['pref']] = 1
        
        if student['programme'] in stats:
            stats[student['programme']] += 1
        else:
            stats[student['programme']] = 1

    return stats

def multiReturnFunc(a,b):
    return a+b, a-b, a*b, a/b

@app.get('/arithmetic/{a}/{b}')
async def arithmetic(a:float, b:float):
    s, t, m, d = multiReturnFunc(a,b)

    return {
        "sum": s,
        "take_away": t,
        "multiply": m,
        "division": d
    } 
