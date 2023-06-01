from flask import Flask
import routes
import os

app = Flask(__name__)
app.register_blueprint(routes.bp)

# Создание папки 'uploads', если она отсутствует
if not os.path.exists(routes.UPLOAD_FOLDER):
    os.makedirs(routes.UPLOAD_FOLDER)

if __name__ == '__main__':
    app.run()
