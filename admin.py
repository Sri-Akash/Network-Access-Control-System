from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client_states = {"192.168.1.33":True, "192.168.1.35":True, "192.168.1.60":True}

@app.route('/')
def admin_page():
    return render_template('admin.html', client_states=client_states)

@app.route('/toggle_client_access', methods=['POST'])
def toggle_client_access():
    client_ip = request.form.get('client_ip')
    if client_ip in client_states:
        client_states[client_ip] = not client_states[client_ip]
        return jsonify({'success': True, 'message': 'Client access toggled successfully'})
    else:
        return jsonify({'success': False, 'message': 'Client not found'})

@app.route('/get_client_state', methods=['GET'])
def get_client_state():
    client_ip = request.args.get('client_ip')
    if client_ip in client_states:
        return jsonify({'success': True, 'enabled': client_states[client_ip]})
    else:
        return jsonify({'success': False, 'message': 'Client not found'})

if __name__ == '__main__':
    app.run(debug=True)
