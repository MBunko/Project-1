from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange
from datetime import datetime


class Games(db.Model):
    Title = db.Column(db.String(300), primary_key=True)
    Release_date = db.Column(db.String(30), nullable=False)
    Genre=db.Column(db.String(30), nullable=False)
    Age_rating= db.Column(db.String(30), nullable=False)
    Description= db.Column(db.String(300), nullable=False)
    reviews= db.relationship("Reviews", backref="games")

class Reviews(db.Model):
    Review_ID = db.Column(db.Integer, primary_key=True)
    Games_title= db.Column(db.String(300), db.ForeignKey('games.Title'), nullable=False)
    Review_title= db.Column(db.String(300), nullable=False)
    Date= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Reviewer_name=db.Column(db.String(30))
    Review_password=db.Column(db.String(30), nullable=False)
    Review=db.Column(db.String(3000), nullable=False)
    Rating=db.Column(db.Integer, nullable=False)


class Add(FlaskForm):
    Title = StringField('Title', validators=[DataRequired()])
    Release_date = DateField('Release date', validators=[DataRequired()])
    Genre=StringField ("Genre", validators=[DataRequired()])
    Age_rating= StringField("Age rating", validators=[DataRequired()])
    Description= StringField("Description", validators=[DataRequired()])
    submit = SubmitField('Add Game')

class Review(FlaskForm):
    Review_title= StringField("Review title")
    Reviewer_name = StringField('Reviewer name')
    Review_password = StringField('Password to edit review', validators=[DataRequired()])
    Review=StringField ("Review- Max 3000 characters", validators=[DataRequired()])
    Rating= IntegerField("Rating out of 10", validators=[DataRequired(), NumberRange(1,10)])
    submit = SubmitField('Add Review')

class Delete(FlaskForm):
    Review_password = StringField('Password to edit review', validators=[DataRequired()])
    submit= SubmitField("Delete Review")

class Update(FlaskForm):
    Review_password = StringField('Password to edit review', validators=[DataRequired()])
    submit= SubmitField("Update Review")