from flask import Flask, request, jsonify
from db import connect_to_mysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有源的请求访问该应用

# 在每次请求开始时建立数据库连接
@app.before_request
def before_request():
    request.connection = connect_to_mysql()

# 在每次请求处理完毕后关闭游标，并提交事务
@app.teardown_request
def teardown_request(exception):
    if hasattr(request, 'connection'):
        connection = request.connection
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.close()
        connection.close()

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/getUserByEmail', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Missing email parameter'}), 400
    
    cursor = request.connection.cursor()
    
    try:
        # 执行 SQL 查询
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            user_data = {
                'id': user[0],
                'kita_id': user[1],
                'email': user[2],
                'password': user[3],
                'name': user[4],
            }
            return jsonify(user_data)
        else:
            return jsonify({'error': 'User not found'})
    except Exception as e:
        print("Error fetching user data:", e)
    finally:
        # 游标会在 teardown_request 函数中关闭
        pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
