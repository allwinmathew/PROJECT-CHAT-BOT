from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Define responses for each cognitive bias
biases_responses = {
    "cognitive bias": "Cognitive bias is a systematic pattern of deviation from norm or rationality in judgment, whereby inferences may be illogical.",
    "halo effect": "The halo effect is a cognitive bias where the perception of one positive trait influences the overall perception of a person or thing.",
    "hindsight bias": "Hindsight bias is the tendency to see events as having been predictable after they have already occurred.",
    "anchoring bias": "Anchoring bias is a cognitive bias where individuals rely too heavily on the first piece of information they receive (the 'anchor') when making decisions.",
    "self-serving bias": "Self-serving bias is the habit of attributing positive events to one's own character but attributing negative events to external factors.",
    "illusion of control": "The illusion of control is the tendency for people to overestimate their ability to control events, even when they have no influence over them.",
    "confirmation bias": "Confirmation bias is the tendency to search for, interpret, or remember information in a way that confirms one's preconceptions, leading to statistical errors."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve the username and password from the form
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username and password match the predefined values
        if username == correct_username and password == correct_password:
            return redirect(url_for('chat.html'))  # Redirect to chat page if login is successful
        else:
            return render_template('login.html', error="Incorrect username or password.")  # Return error if login fails
    
    return render_template('login.html') 

@app.route('/chat')
def chat():
    return render_template('chat.html')

# Endpoint to handle user input and send chatbot response
@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message', '').lower()
    
    # Check if the message contains any cognitive bias keywords
    for bias in biases_responses:
        if bias in user_message:
            return jsonify({'response': biases_responses[bias]})
    
    # Default response if no bias was detected
    return jsonify({'response': "I'm here to assist you with cognitive biases. Please ask about a specific bias!"})

if __name__ == '__main__':
    app.run(debug=True)
