from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
	return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
	# 从HTTP请求拿到用户数据
	for k, v in request.form.items():
		print(k, v)
	# 需要从request对象读取表单内容
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return render_template('signin-ok.html', username=request.form['username'])
	else:
		return render_template('form.html', message='wrong name or password', username=request.form['username'])


if __name__ == '__main__':
	app.run()
