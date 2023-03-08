function on_select(id) {
    let editor = document.getElementById(id);

    // Check if div has tag 'selected'
    if (editor.classList.contains('selected')) {
        // Remove tag
        editor.classList.remove('selected');
    } else {
        // Add tag
        editor.classList.add('selected');
    }
}

function on_click_edit(e) {
    // Check if parent div has class saved
    if (e.target.parentElement.classList.contains('saved')) {
        // Remove class
        e.target.parentElement.classList.remove('saved');

        // Change button text
        e.target.innerHTML = 'Save';

        // Add event listener to save button
        e.target.addEventListener('click', save_question);
        e.target.removeEventListener('click', enable_edit);
    } else {
        // Add class
        e.target.parentElement.classList.add('saved');

        // Change button text
        e.target.innerHTML = 'Edit';

        // Remove event listener from save button
        e.target.removeEventListener('click', save_question);
        e.target.addEventListener('click', enable_edit);
    }

    e.stopPropagation();
}