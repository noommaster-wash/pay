from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# --- ตั้งค่าส่วนสั่งงาน IoT ---
IOT_API_URL = "ใส่_URL_ของอุปกรณ์_IoT_คุณที่นี่"

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    
    # 1. รับข้อมูล
    amount = data.get('amount')
    txn_id = data.get('transaction_id')
    
    print(f"ได้รับเงิน: {amount} บาท | รหัส: {txn_id}")
    
    # 2. สั่งงาน IoT
    try:
        requests.get(IOT_API_URL) # ส่งสัญญาณไปสั่งงานอุปกรณ์
        print("สั่งงาน IoT สำเร็จ")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการสั่ง IoT: {e}")
        
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run()
