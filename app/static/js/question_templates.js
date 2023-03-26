// When template card is clicked, redirect to the template page
function templateCardClicked(templateId) {
    window.location.href = "/templates/" + templateId;
}

// When remove question button is clicked, remove the question from the template
function removeQuestionClicked(questionId, templateId) {
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