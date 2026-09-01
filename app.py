from flask import Flask

from routes.health import health_bp
from routes.translate import translate_bp
from routes.analyze import analyze_bp
from routes.batch import batch_bp

app = Flask(__name__)

app.register_blueprint(health_bp)
app.register_blueprint(translate_bp)
app.register_blueprint(analyze_bp)
app.register_blueprint(batch_bp)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )