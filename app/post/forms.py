from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed
from wtforms.widgets import CheckboxInput, ListWidget

type_choices = [("news", "News"), ("publication", "Publication"),("coding", "Coding"), ("other", "Other")]
enabled_choices = [(True, "True"), (False, "False")]


class PostForm(FlaskForm):
    title = StringField(
        label="Title", validators=[DataRequired(message="This field is required.")]
    )
    text = TextAreaField(
        label="Write your post here",
        render_kw={"rows": 13, "cols": 11},
        validators=[DataRequired(message="This field is required.")],
    )
    image = FileField(
        "Post Picture",
        validators=[FileAllowed(["jpg", "png"], message="This file is not allowed")],
    )
    type = SelectField(
        "Type",
        choices=type_choices,
        validators=[DataRequired(message="Please select a type.")],
    )
    category = SelectField('Category', validators=[DataRequired(message="This field is required.")])
    submit = SubmitField("Submit")


class EditPostForm(FlaskForm):
    title = StringField(label="Title")
    text = TextAreaField(label="Write your post here", render_kw={"rows": 13, "cols": 11},)
    image = FileField(
        "Post Picture",
        validators=[FileAllowed(["jpg", "png"], message="This file is not allowed")],
    )
    type = SelectField("Type", choices=type_choices)
    enabled = SelectField("Enabled", choices=enabled_choices)
    category = SelectField('Category')
    submit = SubmitField("Submit")
    
class CategoryForm(FlaskForm):
    name = StringField("Category name",
                       validators=[DataRequired(message="This field is required."),])
    submit = SubmitField("Submit")
    
class EditCategoryForm(FlaskForm):
    name = StringField("Category name",
                       validators=[DataRequired(message="This field is required."),])
    submit = SubmitField("Submit")
