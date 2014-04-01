Flask-DjangoQuery
=================

A module that implements a more Django like interface for Flask-SQLAlchemy query objects.  It's still API compatible with the regular one but extends it with Djangoisms.

## Usage

```python
from flask import Flask
from flask.ext.djangoquery import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
db.init_app(app)
```

Then you can use it just like Flask-SQLAlchemy.

### Define a model

```python
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.Datetime)
    title = db.Column(db.String(50))

## Example queries

```python
Post.query.filter_by(pub_date__year=2008)
Post.query.exclude_by(id=42)
Post.query.filter_by(title__contains='something')
Post.query.order_by('-post__pub_date')
```