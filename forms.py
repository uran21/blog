import wtforms.validators
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("email", validators=[DataRequired(), wtforms.validators.Email()])
    password = PasswordField("password", validators=[DataRequired(), wtforms.validators.Length(min=8)])
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("Register User")

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit=SubmitField("Login")

class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Leave a comment")