from flask import Flask, render_template
import pymysql

app = Flask(__name__)

# Configuration de la base de données
db = pymysql.connect(host='localhost', user='root', password='', database='module_164_diego_besse')
#hjhgj
@app.route('/')
def afficher_donnees():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM t_joueurs')
    data = cursor.fetchall()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()