from flask import *
from github import Github
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def start():
	return render_template('login.html')

@app.route('/login',methods = ['GET'])
def login():
	user = request.args.get('username')
	passw = request.args.get('password')
	try:
		g = Github(user,passw)
		data = [(s.name, s.name) for s in g.get_user().get_repos()]
		return render_template('hello.html',name = user)
	except:
		return 'Incorrect username or password'


@app.route('/perform',methods = ['GET'])
def perform():
	user =  request.args.get('user')
	repo = request.args.get('repo_name')
	r = user.create_repo(repo)
	return "repo created"
	

if __name__ == '__main__':
	app.run(debug = True)