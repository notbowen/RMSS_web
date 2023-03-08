from app.extensions import db


class Question(db.Model):
    id = db.Column(db.String(30), primary_key=True)
    is_mcq = db.Column(db.Boolean, nullable=False)
    content = db.Column(db.JSON, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("questions", lazy=True))

    def __repr__(self):
        return f"<Question {self.id}>"

# Sample Data:
# {'editorjs': {'time': 1678073534428, 'blocks': [{'id': '1ergnfLPRX', 'type': 'paragraph',
# 'data': {'text': '\nA scientist crafted an experiment and stated her hypothesis. However, after conducting the
# experiment, the results showed that her hypothesis was wrong.\n\n', 'alignment': 'left'}}, {'id': 'aiGqe2ojlv',
# 'type': 'paragraph', 'data': {'text': 'What should the scientist do with the results?', 'alignment': 'left'}},
# {'id': 'e4dL0Tt246', 'type': 'paragraph', 'data': {'text': '\n<b>A</b>&nbsp; Change the results so that her
# hypothesis is correct.<br><b>B</b>&nbsp; Conclude that her hypothesis was false.<br><b>C</b>&nbsp; Ignore the
# results because they did not fit her hypothesis.<br><b>D</b>&nbsp; Repeat the experiment until her hypothesis is
# proven right.\n\n', 'alignment': 'left'}}], 'version': '2.26.5'}, 'question_id': 'AES_2020_A_1', 'question_type':
# 'MCQ', 'answer': 'B'}
