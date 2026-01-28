from flask import Flask, session, redirect, url_for, request, render_template_string

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management

# Define user roles with priorities
USER_PRIORITIES = {
    'admin': 3,
    'member': 2,
    'guest': 1
}

# Example user data (in a real application, use a database)
users = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'member': {'password': 'memberpass', 'role': 'member'},
    'guest': {'password': 'guestpass', 'role': 'guest'}
}

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        user_role = session['role']
        return f'Logged in as {username} with role {user_role}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            session['priority'] = USER_PRIORITIES[session['role']]
            return redirect(url_for('home'))
        return 'Invalid credentials'
    return render_template_string('''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    ''')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    session.pop('priority', None)
    return redirect(url_for('home'))

# Middleware to enforce session priority (example)
@app.before_request
def enforce_priority():
    if 'priority' in session:
        # Example priority check, can be extended with more logic
        # Here we just print the current user's priority
        print(f'Current session priority: {session["priority"]}')
        if session['priority'] == 2:
            session['priority'] = 1  # This downgrades member to guest priority
        
        # Here we can add logic to manage sessions based on priority
        pass

if __name__ == '__main__':
    app.run(debug=True)