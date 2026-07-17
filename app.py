from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
   return "Hello from the CI/CD pipeline! Deployed automatically by Jenkins. 12345\n"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
