import docx
from haggis.files.docx import list_number
import re

from app.models.question import Question
from typing import List, Dict


class HTMLHelper(object):
    """ Translates some html into word runs. """

    def __init__(self):
        self.get_tags = re.compile(
            "(<[a-z,A-Z]+>)(.*?)(</[a-z,A-Z]+>)", flags=re.DOTALL)

    def html_to_run_map(self, html_fragment):
        """ Breaks an html fragment into a run map """
        ptr = 0
        run_map = []
        for match in self.get_tags.finditer(html_fragment):
            if match.start() > ptr:
                text = html_fragment[ptr:match.start()]
                if len(text) > 0:
                    run_map.append((text, "plain_text"))
            run_map.append((match.group(2), match.group(1)))
            ptr = match.end()
        if ptr < len(html_fragment) - 1:
            run_map.append((html_fragment[ptr:], "plain_text"))
        return run_map

    def insert_runs_from_html_map(self, paragraph, run_map):
        """ Inserts some runs into a paragraph object. """
        for run_item in run_map:
            run = paragraph.add_run(run_item[0])
            if run_item[1] == "<b>":
                run.bold = True


def parse_questions(questions: Dict[str, List[Question]], doc: docx.Document) -> None:
    """Parse sorted questions into a docx document

    Args:
        sorted_questions (Dict[str, List[Question]]): Dict of questions with section as key
        doc (docx.Document): docx document to write to
    """

    # Parse MCQ questions
    parse_mcq_question(questions["A"], doc)

    # Parse structured questions
    parse_structured_question(questions["B"], doc)
    parse_structured_question(questions["C"], doc)

    # Add MCQ answers
    add_mcq_answers(questions["A"], doc)

    # Add structured answers
    add_structured_answers(questions["B"], doc)
    add_structured_answers(questions["C"], doc)


def parse_mcq_question(questions: List[Question], doc: docx.Document) -> None:
    """Parse a multiple choice question into a docx document

    Args:
        qn_no (int): Question number
        question (Question): MCQ Question to parse
        doc (docx.Document): docx document to write to
    """

    # Return if no questions
    if len(questions) == 0:
        return
    
    # Add "root" paragraph
    prev_root = doc.add_paragraph()
    prev_root.paragraph_format.left_indent = docx.shared.Cm(0.5)

    # Initialise HTML helper
    html_helper = HTMLHelper()

    # Loop through and add questions
    for i, question in enumerate(questions):
        # Add question number
        if i == 0:
            root = prev_root
        else:
            root = doc.add_paragraph()
            root.paragraph_format.left_indent = docx.shared.Cm(0.5)

        # Add question
        for block in question.content["blocks"]:
            if block["type"] == "paragraph":
                text = process_text(block["data"]["text"])  # Process text
                run_map = html_helper.html_to_run_map(text)
                html_helper.insert_runs_from_html_map(root, run_map)  # Add text to paragraph
                root.add_run("\n\n")  # Add new line

        # Make paragraph a list to have numbering
        if i != 0:
            list_number(doc, root, prev=prev_root)
        else:
            list_number(doc, root)


def parse_structured_question(questions: List[Question], doc: docx.Document) -> None:
    """Parse a structured question into a docx document

    Args:
        qn_no (int): Question number
        question (Question): Structured Question to parse
        doc (docx.Document): docx document to write to
    """
    
    # Return if no questions
    if len(questions) == 0:
        return

    pass


def add_mcq_answers(questions: List[Question], doc: docx.Document) -> None:
    """Add MCQ answers to a docx document

    Args:
        questions (List[Question]): List of questions
        doc (docx.Document): docx document to write to
    """

    # Return if no questions
    if len(questions) == 0:
        return

    pass


def add_structured_answers(questions: List[Question], doc: docx.Document) -> None:
    """Add structured answers to a docx document

    Args:
        questions (List[Question]): List of questions
        doc (docx.Document): docx document to write to
    """

    # Return if no questions
    if len(questions) == 0:
        return

    pass

def process_text(text: str) -> str:
    text = text.replace("&nbsp;", " ")
    text = text.replace("<br>", "\n")
    text = text.replace("<b></b>", "")
    text = text.strip("\n")

    return text
