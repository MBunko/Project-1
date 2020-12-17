from application import app, db
from application.models import Games, Add, Reviews, Review
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

@app.route('/add', methods=["GET", "POST"])
def add():
    form=Add()
    if request.method == 'POST':

        if not form.validate_on_submit():
            return render_template('adderror.html', form=form, title="New Game")
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

@app.route('/review/<Title>', methods=["GET", "POST"])
def review(Title):
    form=Review()
    if request.method == 'POST':

        if not form.validate_on_submit():
            return render_template('reviewerror.html', form=form, title="New Game")
        else:
            new_review = Reviews(Games_title=Title, Reviewer_name=form.Reviewer_name.data, Review_password=form.Review_password.data, Review=form.Review.data, Rating= form.Rating.data)
            db.session.add(new_review)
            db.session.commit()
            return redirect(url_for("game", Title=new_review.Games_title))
    return render_template('review.html', form=form, title="New Game")