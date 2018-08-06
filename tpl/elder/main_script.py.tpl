from click import echo
from application import app, db

@app.cli.command()
def initdb():
    """Initialize the database."""
    db.create_all()
    echo('Init the db')

if __name__ == "__main__":
    print("This script is not intended for direct run. Use global flask script instead.")