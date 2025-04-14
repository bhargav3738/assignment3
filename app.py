from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Format the current time in a human-readable format.
    current_time = datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
    
    # HTML template with in-line CSS and Bootstrap for styling.
    html = """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bhargav | DevOps Showcase</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
        <style>
          body {
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(135deg, #1f4037, #99f2c8);
            color: #fff;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
          }
          .glass-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 20px;
            padding: 40px;
            width: 100%;
            max-width: 600px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
          }
          .btn-custom {
            border-radius: 30px;
            padding: 10px 30px;
            font-size: 1rem;
            transition: background-color 0.3s, color 0.3s;
          }
          .btn-custom:hover {
            background-color: #fff;
            color: #1f4037;
          }
          .quote {
            font-style: italic;
            color: #f1f1f1;
            margin-top: 25px;
            font-size: 1rem;
          }
        </style>
      </head>
      <body>
        <div class="glass-card text-center">
          <h1 class="display-5 fw-bold mb-3">🚀 Bhargav Nimbalkar</h1>
          <p class="lead">DevOps Test #2 | <strong>AWS ECS Fargate Deployment</strong></p>
          <span class="badge bg-success fs-6 mb-3">Status: LIVE</span>
          <p>⏰ Server Time: <strong>{{ current_time }}</strong></p>
          <a href="/" class="btn btn-outline-light btn-custom mt-3">🔁 Refresh</a>
          <div class="quote">"Success usually comes to those who are too busy to be looking for it."</div>
        </div>
      </body>
    </html>
    """
    return render_template_string(html, current_time=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
