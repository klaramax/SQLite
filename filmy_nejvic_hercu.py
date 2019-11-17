import sqlite3

dotaz = """
SELECT movie.name AS movie_name,
       COUNT(actor.id) AS pocet_hercu

FROM movie
JOIN movie_to_actor ON movie_to_actor.movie_id = movie.id
JOIN actor ON movie_to_actor.actor_id = actor.id
GROUP BY movie.name
ORDER BY pocet_hercu;
"""

import flask
app = flask.Flask(__name__)
@app.route('/')
def index():
    con = sqlite3.connect('D:\\SQL\\app.db')
    rows = [
        f'<tr><td>{film}</td><td>{pocet}</td></tr>'
        for film, pocet in con.execute(dotaz)
    ]
    return f'''
        <h1>Filmy s nejvíce herci</h1>
        <table>
        {''.join(rows)}
        </table>
    '''

app.run()