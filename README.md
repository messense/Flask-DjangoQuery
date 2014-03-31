Flask-DjangoQuery
=================

Django like query extension for Flask-SQLAlchemy

## Usage

```python
from flask import Flask
from flask.ext.djangoquery import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()
db.init_app(app)
```

Then you can use it just like Flask-SQLAlchemy
