from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_person', methods=['POST'])
def get_person():
    name = request.form['name']
    person_images = {
        "Baris": "bp.jpg",
        "Masi": "masi.jpg",
        "Fatih": "fati.jpg",
        "Furkan": "furki.jpg",
        "Sirin": "sirin.jpg",
        "Betul": "betul.jpg",
        "Mehmet": "memo.jpg",
        "Bugra": "mugom.jpg",
    }
    image_url = person_images.get(name, None)
    return render_template('result.html', name=name, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)

