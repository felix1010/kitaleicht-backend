from flask import Flask, request, jsonify
from db import connect_to_db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许所有源的请求访问该应用
connection = connect_to_db()


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/getUserByEmail', methods=['GET'])
def get_user_by_email():
    email = request.args.get('email')
    cursor = connection.cursor()
    
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
            return jsonify({'message': 'User not found'})
    except Exception as e:
        print("Error fetching user data:", e)
    finally:
        # 关闭游标
        cursor.close()


if __name__ == '__main__':
    app.run(debug=True)
