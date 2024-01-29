from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    current_time = time.strftime('%I:%M:%S %p')
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', time=current_time, date=current_date)

if __name__ == '__main__':
    app.run(debug=True)
