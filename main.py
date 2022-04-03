from flask import Flask, render_template
from json import load

with open("template.json", "r") as f:
    config = load(f)


# Create a flask project
app = Flask(
    __name__,
    template_folder=config["template"], 
    static_folder=config["static"]
)

# Create a first and end url
@app.route(
    rule="/",
)
def index():
    return render_template("/html/index.html")

@app.route(
    rule="/privacy"
)
def privacy():
    return render_template("/html/privacy_policy.html")


if __name__ == "__main__":
    app.run(
        debug=True
    )