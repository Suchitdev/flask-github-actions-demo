from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 GitHub Actions CI Pipeline - Version 2"
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Demo App</title>
        <style>
            body {
                background: linear-gradient(135deg, #4facfe, #00f2fe);
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .card {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
                width: 400px;
            }

            h1 {
                color: #2c3e50;
            }

            p {
                color: #555;
                font-size: 18px;
            }

            .status {
                margin-top: 20px;
                display: inline-block;
                background: #28a745;
                color: white;
                padding: 10px 20px;
                border-radius: 25px;
                font-weight: bold;
            }

            footer {
                margin-top: 25px;
                color: #777;
                font-size: 14px;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🚀 DevOps Demo App</h1>

            <p>Welcome to your first GitHub Actions + Docker project.</p>

            <div class="status">
                ✅ Application Running Successfully
            </div>

            <footer>
                Built  using Flask
            </footer>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)