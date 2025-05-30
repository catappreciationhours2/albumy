from albumy import create_app


app = create_app()

app = create_app()

with app.app_context():
    from albumy.extensions import db
    db.create_all()  # remove this after first deploy

