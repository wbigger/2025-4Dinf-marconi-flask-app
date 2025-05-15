import os

from flask import Flask, send_file, render_template

app = Flask(__name__,template_folder='src')


posts=[
    {'title': "Primo post", 'content': "Questo è il contenuto del primo post."},
    {'title': "Secondo post", 'content': "Questo è il contenuto del secondo post."},
    {'title': "Terzo post", 'content': "Questo è il contenuto del terzo post."}
]

@app.route("/")
def index():
    return render_template('index.html', posts=posts)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
