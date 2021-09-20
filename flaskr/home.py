from flask import Blueprint, render_template
from git import Repo
import os

bp = Blueprint('home', __name__, url_prefix='/home' )
# creates a blueprint named home. url_prefix will be prepended to all the URLS associated with the blueprint

repo = Repo(os.path.dirname(os.path.dirname(os.path.realpath(__file__)) ) )
print(repo)
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
print(tags)
gittag = str(tags[-1])
print(gittag)

@bp.route('/home')
def home():
    repo = Repo(os.path.realpath(__file__))
    print(repo)
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    gittag = str(tags[-1])
    print(gittag)
    return render_template('home/home.html', gittag=gittag)
