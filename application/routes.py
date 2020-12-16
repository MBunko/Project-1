from application import app, db
from application.models import Games, Add
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

@app.route('/add', methods=["GET", "POST"])
def add():
    form=Add()
    if request.method == 'POST':

        if not form.validate_on_submit():
            return "Please supply both task name and status"
        else:
            new_game = Games(Title=form.Title.data, Release_date=form.Release_date.data, Genre=form.Genre.data, Age_rating=form.Age_rating.data, Description= form.Description.data)
            db.session.add(new_game)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('add.html', form=form, title="New Game")

@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def home():
    all_games = Games.query.all()
    
    return render_template("index.html", title="Home", all_games=all_games)


@app.route('/game/<Title>', methods= ["GET", "POST"])
def game(Title):
    form=Add()
    game = Games.query.filter_by(Title=Title).first()
    return render_template("update.html", form=form, title=Title, game=game)