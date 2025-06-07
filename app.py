from flask import Flask, render_template, request, redirect, url_for
from ftplib import FTP

app = Flask(__name__)

FTP_HOST = 'a-717.myddns.me'
FTP_PORT = 1157
FTP_USER = 'Web_server'
FTP_PASS = 'Thien180793@'
FTP_DIR = '/H/ANH_CA_NHAN_THIEN/minh phu'

@app.route('/home')
def home():
    ftp = FTP()
    ftp.connect(FTP_HOST, FTP_PORT)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(FTP_DIR)
    directories = ftp.nlst()
    ftp.quit()
    return render_template('home.html', directories=directories)

def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == 'user1' and password == 'pass1':
        return redirect(url_for('home'))
    elif username == 'user2' and password == 'pass2':
        return redirect(url_for('home'))
    else:
        return 'Đăng nhập thất bại!'

@app.route('/home')
def home():
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(FTP_DIR)
    directories = ftp.nlst()
    ftp.quit()
    return render_template('home.html', directories=directories)

@app.route('/view_images/<directory>')
def view_images(directory):
    ftp = FTP(FTP_HOST)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(f"{FTP_DIR}/{directory}")
    images = ftp.nlst()
    ftp.quit()
    return render_template('view_images.html', images=images, directory=directory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
