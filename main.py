import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route("/",methods=['Get'])
def home():
    return "<center><h1> Welcome to my API Assignment!</h1> <br><h2> Name: Smart Patel</h2></center>"


@app.route('/snowboard/insert', methods=['POST'])
def create_snowboard():
    
    try:        
        _json = request.get_json()
        print(_json)
        _boardtype = _json['boardtype']
        _brand = _json['brand']
        _msrp = _json['msrp']	
        _size = _json['size']	

        if _boardtype and _brand and _msrp and _size and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO snowboard(boardtype, brand, msrp, size) VALUES( %s, %s, %s, %s)"
            bindData = (_boardtype, _brand, _msrp, _size)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            cursor.close() 
            conn.close()
            respone = jsonify('Data Inserted successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
        return str(err)          
    
@app.route('/snowboard', methods=['GET'])
def snowboard():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, boardtype, brand, msrp, size FROM snowboard")
        snowboardRows = cursor.fetchall()
        respone = jsonify(snowboardRows)
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/snowboard/update', methods=['PUT'])
def update_snowboard():
    try:
        _json = request.json
        _id = _json['id']
        _boardtype = _json['boardtype']
        _brand = _json['brand']
        _msrp = _json['msrp']	
        _size = _json['size']
        if _id and _boardtype and _brand and _msrp and _size and request.method == 'PUT':			
            sqlQuery = "UPDATE snowboard SET boardtype=%s, brand=%s, msrp=%s, size=%s WHERE id=%s"
            bindData = (_boardtype, _brand, _msrp, _size, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Snowboard data updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as err:
        print(err)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/snowboard/delete/<int:id>', methods=['DELETE'])
def delete_snowboard(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM snowboard WHERE id=%s", (id,))
        conn.commit()
        respone = jsonify('Snowboard Id deleted successfully!')
        respone.status_code = 200
        return respone
    except Exception as err:
        print(err)
    finally:
        conn.commit()
        cursor.close() 
        conn.close()
        
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()