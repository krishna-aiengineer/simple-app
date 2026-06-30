from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <style>
        body {
            font-family: -apple-system, "Segoe UI", system-ui, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f7f8fa;
            color: #1f2328;
        }
        .card {
            text-align: center;
            padding: 48px 64px;
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
        }
        h1 {
            font-size: 2.5rem;
            margin: 0 0 12px;
        }
        p {
            color: #57606a;
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello, World!</h1>
        <p>Your Flask web app is running successfully.</p>
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
