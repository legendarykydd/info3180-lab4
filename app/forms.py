
from flask_wtf.file import FileAllowed, FileRequired, FileField
from flask_wtf import FlaskForm


class UploadForm(FlaskForm):
    image = FileField('Image', validators = [FileRequired(), FileAllowed(['jpg', 'png'])])