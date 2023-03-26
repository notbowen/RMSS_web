// When template card is clicked, redirect to the template page
function templateCardClicked(templateId) {
    window.location.href = "/templates/" + templateId;
}

// When remove question button is clicked, remove the question from the template
function removeQuestionClicked(questionId, templateId) {
    // Ask user for confirmation
    var confirmation = confirm("Are you sure you want to remove " + questionId + " from the template?");
    if (!confirmation) {
        return;
    }
    
    // Send request to remove question from template
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", "/templates/" + templateId + "/delete_question?id=" + questionId, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState !== 4) {
            return;
        }

        if (xhr.status !== 200) {
            alert("Something went wrong!\nError: " + xhr.responseText);
        } else {
            window.location.reload();
        }
    };

    xhr.send();
}

// When delete template button is clicked, delete the template
function deleteTemplateClicked(templateId) {
    // Ask user for confirmation
    var confirmation = confirm("Are you sure you want to delete this template?");
    if (!confirmation) {
        return;
    }

    // Send request to delete template
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", "/templates/delete?id=" + templateId, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState !== 4) {
            return;
        }

        if (xhr.status !== 200) {
            alert("Something went wrong!\nError: " + xhr.responseText);
        } else {
            window.location.href = "/templates";
        }
    };

    xhr.send();
}
