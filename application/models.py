from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Games(db.Model):
    Title = db.Column(db.String(30), primary_key=True)
    Release_date = db.Column(db.String(30))
    Genre=db.Column(db.String(30))
    Age_rating= db.Column(db.String(30))
    Description= db.Column(db.String(30))
    reviews= db.relationship("Reviews", backref="games")

class Reviews(db.Model):
    Review_ID = db.Column(db.Integer, primary_key=True)
    Games_title= db.Column(db.String(30), db.ForeignKey('games.Title'), nullable=False)
    Reviewer_name=db.Column(db.String(30))
    Review_password=db.Column(db.String(30))
    Review=db.Column(db.String(30))
    Rating=db.Column(db.Integer)



class Add(FlaskForm):
    Title = StringField('Title', validators=[DataRequired()])
    Release_date = StringField('Release date')
    Genre=StringField ("Genre")
    Age_rating= StringField("Age rating")
    Description= StringField("Description")
    submit = SubmitField('Add Entry')