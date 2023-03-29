# RMSS Question Bank

- [RMSS Question Bank](#rmss-question-bank)
  - [Adding Questions](#adding-questions)
    - [Question IDs](#question-ids)
    - [Question Content \& Answer](#question-content--answer)
    - [Saving](#saving)
    - [Saving (Errors)](#saving-errors)
  - [Searching \& Exporting Questions](#searching--exporting-questions)
    - [Searching](#searching)
    - [Exporting](#exporting)
    - [After Exporting](#after-exporting)
  - [Topics](#topics)
    - [Editing Topics](#editing-topics)
    - [Adding Topics](#adding-topics)
  - [Templates](#templates)
    - [Creating Templates](#creating-templates)
    - [Adding Questions to Templates](#adding-questions-to-templates)
    - [Removing Questions from Templates](#removing-questions-from-templates)
    - [Deleting the Entire Template](#deleting-the-entire-template)
    - [Importing Questions from Templates](#importing-questions-from-templates)

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

The page to search and export questions is located at `/questions/search`, or by clicking the `Add to Book` button in the navigation bar.

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

If any errors occur, check if your internet connection is working, and if the server is online.
If both are working, do send me the error logs.

### After Exporting

After exporting to Word, do align the question numbers by right-clicking the first line of the first question, and select `Adjust List Indents`.

Enter `0 cm` for the `Bullet Position`, and `1 cm` for the `Text Indent`. Uncheck `Add tab stop at` too.

Images should also be resized to the appropriate size.

Tables should also be resized and aligned to the right place.

## Topics

The page to edit topics can be found at `/topics/edit`, or by clicking the `Edit Topics` button in the navigation bar.

### Editing Topics

Upon clicking the `Edit` button, you may change the content of the topic.
You **must** click `Save` after editing the topics, or changes will not be applied.

Topics may only be deleted once no questions are saved as that topic.

### Adding Topics

New topics can be added by filling in all the required fields and clicking the `Add Topic` button.

The topics will be displayed under the `category` dropdown when adding or searching for questions, displayed with the format of: `{Topic} ({Subject}, {Level})`

## Templates

Templates can be accessed at `/templates`, or by clicking the `Templates` button in the navigation bar.

### Creating Templates

Templates can be created in the `Selected Questions` sidebar. Simply type the template name into the dropdown that says `None`, and press enter to create the template.

Select all the questions to add to the template and click `Add to Template`

### Adding Questions to Templates

You may add new questions to an existing template by selecting all the questions you want to add, and select the template to add to in the dropdown (that says `None` by defualt), and click the `Add to Template` button.

### Removing Questions from Templates

Navigate to the templates page and click on the template you want to remove the question from.

Find the question to remove and click on the `Remove from Template` button.

### Deleting the Entire Template

You can remove a template by navigating to the template page, and click the `Delete` button corresponding to the template.

You can also remove the template by editing it, and clicking on the `Delete Template` button at the top of the page.

### Importing Questions from Templates

To import questions from a template, select the template you want to import from in the dropdown menu (default `None`).

Then, click the `Import from Template` button. It will prompt you if you would like to overwrite the currently selected questions.

If you want to keep your current questions and add on to it, select `No`.

If you want to delete your current questions and replace them, select `Yes`.
