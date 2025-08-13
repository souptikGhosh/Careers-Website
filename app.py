from flask import Flask, render_template, jsonify

app = Flask(__name__)


Jobs =[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru,India',
    
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Texas,USA',
    'salary':'$120,000'
  },

  {
    'id':3,
    'title': 'Machine Learning Engineer',
    'location':'London,United Kingdom',
    'salary':'£63,000'
  },
  {
    'id':4,
    'title': 'Fullstack Developer',
    'location':'Kyoto,Japan',
    'salary': '¥9,000,000'
  },
]
@app.route('/')
def hello_world():
  return render_template('home.html', jobs=Jobs, company_name='Adobe')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs)


print(__name__)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
