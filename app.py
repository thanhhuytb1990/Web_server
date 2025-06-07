from flask import Flask, render_template, request, redirect, url_for
from ftplib import FTP

app = Flask(__name__)

FTP_HOST = 'a-717.myddns.me'
FTP_PORT = 1157
FTP_USER = 'Web_server'
FTP_PASS = 'Thien180793@'
FTP_DIR = '/H/ANH_CA_NHAN_THIEN/minh phu'

# Giao diện đăng nhập
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

# Xử lý đăng nhập
@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if (username, password) in [('user1', 'pass1'), ('user2', 'pass2')]:
        return redirect(url_for('home'))
    else:
        return 'Đăng nhập thất bại!'

# Trang chính sau đăng nhập
@app.route('/home')
def home():
    try:
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT, timeout=10)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.cwd(FTP_DIR)
        items = ftp.nlst()
        ftp.quit()
        return render_template('home.html', directories=items)
    except Exception as e:
        return f"Lỗi khi kết nối FTP: {e}"

# Xem hình ảnh trong thư mục con
@app.route('/view_images/<path:directory>')
def view_images(directory):
    try:
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT, timeout=10)
        ftp.login(FTP_USER, FTP_PASS)
        full_path = f"{FTP_DIR}/{directory}"
        ftp.cwd(full_path)
        files = ftp.nlst()
        images = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        ftp.quit()
        return render_template('view_images.html', images=images, directory=directory)
    except Exception as e:
        return f"Lỗi khi tải hình ảnh: {e}"

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000, debug=True)
