from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No data"}), 400
    
    # ดึงข้อมูลจาก SCB (สมมติชื่อ field ตามมาตรฐานทั่วไป)
    amount = data.get('amount')
    txn_id = data.get('transaction_id')
    print(f"ได้รับเงิน {amount} บาท | รหัส {txn_id}")
    
    # --- ตรงนี้คือจุดที่เราจะสั่งงาน IoT ในอนาคต ---
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run()
