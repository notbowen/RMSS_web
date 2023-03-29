# RMSS Question Bank

## Table of Contents

- [RMSS Question Bank](#rmss-question-bank)
  - [Table of Contents](#table-of-contents)
  - [Adding Questions](#adding-questions)
    - [Question IDs](#question-ids)
    - [Question Content \& Answer](#question-content--answer)
    - [Saving](#saving)
    - [Saving (Errors)](#saving-errors)
  - [Searching \& Exporting Questions](#searching--exporting-questions)
    - [Searching](#searching)
    - [Exporting](#exporting)

## Adding Questions

Questions are added in the home page, located at `/`.

### Question IDs

7 inputs are provided to create the question ID and identify the question source, type, and category.

`School`:
The abbreviation of the school name, e.g: `AES`

`Level`:
The level of the **paper** which the question is sourced from.

`Test`:
E.g `WA1`, `WA2`, `EOY`, `MYE`.

`Year`:
The year of the **paper** which the question was sourced from.

`Question No.`: The question number.

`Section`:
The section the question belongs to.
This will be used as a search filter.

`Category`:
The topic/category the question belongs to.
This will be used as a search filter.

### Question Content & Answer

2 rich text boxes are provided to input question data inside.
Data can be inserted by clicking on an empty space below, or by clicking the `+` icon on the right side.

The `+` icon will list `3` options:

1. Text
   - Normal text with options to **bold** and *italicise* the text.
   - Text is aligned to the left by default.
   - Upon clicking the 6 dots, `left`, `center` and `right` alignment options will be made available.
2. Table
   - Rows and columns can be added by clicking the `+` icons inside the table cells.
   - If the `with heading` option is enabled, the first column of the table will be shaded gray.
   - Text inside the table may be styled **bold** and *italic*
3. Image
   - Image options do not work, and images have to be adjusted after export.
   - Images are aligned to the center by default.

### Saving

Once the save button is clicked, it should clear the content inside the rich text editors, but keep the Question ID values.

If saving was successful, a alert should show up informing you that it succeeded.

### Saving (Errors)

The server may have gone down, or your internet connection may be faulty.

If both are working, do send me the error message and I will try to fix it asap.

## Searching & Exporting Questions

The page to search and export questions is located at `/questions/search`.

### Searching

There are `2` fields to filter questions by:

|Field|Content|
|-----|-------|
|Section|Questions under section `A` are MCQ questions while `B` & `C` are structured questions|
|Topic|The topic which the question is classified by. Topics can be edited under the topic page.|

### Exporting

Once you have found the question, click on it to select it into the export sidebar.

Once all questions are present, click `Export to Word` and upload the file to append the questions to.

If no errors occur, a Word file with the filename `questions.docx` should be returned. Feel free to rename it and save.
