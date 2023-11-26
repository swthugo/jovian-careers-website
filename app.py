from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
      'id': 1,
      'title' : 'Data Analyst',
      'location': 'Hong Kong',
      'salary': 'HK$23,000',
    },
    {
      'id': 2,
      'title' : 'Web Designer',
      'location': 'Hong Kong',
      'salary': 'HK$20,000',
    },
    {
      'id': 3,
      'title' : 'Frontend Developer',
      'location': 'Hong Kong',
      'salary': 'HK$25,000',
    },
    {
      'id': 4,
      'title' : 'Backend Developer',
      'location': 'Hong Kong',
      'salary': 'HK$30,000',
    }
]

@app.route("/")
def index():
    return render_template('index.html', jobs=jobs)
    # return "<p>Hello, World!</p>"

@app.route("/jobs")
def list_jobs():
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)