import numpy as np
import pandas as pd

from flask import (Flask, render_template)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5002)
