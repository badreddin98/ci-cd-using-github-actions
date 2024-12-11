from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    if not data or 'numbers' not in data:
        return jsonify({'error': 'Invalid input'}), 400
    
    numbers = data['numbers']
    if not isinstance(numbers, list):
        return jsonify({'error': 'Numbers must be a list'}), 400
    
    if not all(isinstance(n, (int, float)) for n in numbers):
        return jsonify({'error': 'All elements must be numbers'}), 400
    
    result = sum(numbers)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
