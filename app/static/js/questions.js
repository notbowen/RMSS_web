// On select div, add a selected class to the selected option
function on_select(id) {
    let question_div = document.getElementById(id);

    // If the div is already selected, deselect it and vice-versa
    if (question_div.classList.contains("selected")) {
        remove_question_by_id(id);
    } else {
        add_question_by_id(id);
    }
}

// Make function global
window.on_select = on_select;

// On delete button click, ask for confirmation and delete selected questions
function on_delete(id) {
    if (
        confirm(
            "Are you sure you want to delete this question?\nAction is irreversible!\nQuestion ID: " +
                id
        ) === true
    ) {
        // URL
        let url = build_url_with_params("/api/question/delete?id=" + id);
        location.href = url;
    }
}

// Make function global
window.on_delete = on_delete;

// On edit button click
function on_edit(id) {
    // URL
    let url = build_url_with_params("/questions/edit?id=" + id);
    location.href = url;
}

window.on_edit = on_edit;

// Build URL with params
function build_url_with_params(url) {
    // Get search params
    let section = new URLSearchParams(window.location.search).get("section");
    let category = new URLSearchParams(window.location.search).get("category");

    // If section is not empty, add it to the url
    if (section !== null) {
        url += "&section=" + section;
    }

    // If category is not empty, add it to the url
    if (category !== null) {
        url += "&category=" + category;
    }

    return url;
}

// On search button click, search for questions
document.getElementById("search-btn").addEventListener("click", function () {
    // Get value of section-select
    let section = document.getElementById("section-select").value;

    // Get value of category-select
    let category = document.getElementById("category-select").value;

    // Submit GET request to /questions/search with section and category as query parameters
    let url = "/questions/search";

    // If section is not empty, add it to the url
    if (section !== "") {
        url += "?section=" + section;
    }

    // If category is not empty, add it to the url
    if (category !== "") {
        if (url.includes("?")) {
            url += "&category=" + category;
        } else {
            url += "?category=" + category;
        }
    }

    // Redirect to the url
    location.href = url;
});

// Add filtering to the selects
$("#section-select").chosen({ width: "65px" });
$("#category-select").chosen();

// Slide div in and out on click
$(document).ready(function () {
    var slider_width = $(".selected-questions").width();
    $("#toggle-sel-qns").click(function () {
        if (
            $(this).css("margin-right") == slider_width + "px" &&
            !$(this).is(":animated")
        ) {
            $(".selected-questions,#toggle-sel-qns").animate({
                "margin-right": "-=" + slider_width,
            });
        } else {
            if (!$(this).is(":animated")) {
                // prevent double click to double margin
                $(".selected-questions,#toggle-sel-qns").animate({
                    "margin-right": "+=" + slider_width,
                });
            }
        }
    });
});

// Remove question from selected questions on click
$(document).on("click", ".selected-questions p", function () {
    // Get question id
    let id = $(this).text();

    // Ask user for confirmation
    if (!confirm("Are you sure you want to remove " + id + " from the list of selected questions?")) {
        return;
    }

    // Remove question from selected questions array
    remove_question_by_id(id);
});

// Function to add a question to the selected questions array
function add_question_by_id(id) {
    // Add question to selected questions array
    let selected_questions = JSON.parse(
        localStorage.getItem("selected_questions")
    );
    selected_questions.push(id);
    localStorage.setItem("selected_questions", JSON.stringify(selected_questions));

    // Add to selected questions div
    let selected_questions_div = document.getElementById(
        "selected-questions-list"
    );
    selected_questions_div.innerHTML += "<p>" + id + "</p>";

    // Add selected class to question div
    let question_div = document.getElementById(id);
    if (question_div !== null) {
        question_div.classList.add("selected");
    }

    // Show number of selected questions
    $("#sel-qns-h2").text(selected_questions.length + " Selected Question(s)");
}

// Function to remove a question from the selected questions array
function remove_question_by_id(id) {
    // Remove question from selected questions array
    let selected_questions = JSON.parse(
        localStorage.getItem("selected_questions")
    );
    let index = selected_questions.indexOf(id);
    if (index > -1) {
        selected_questions.splice(index, 1);
    }
    localStorage.setItem("selected_questions", JSON.stringify(selected_questions));

    // Remove from selected questions div
    let selected_questions_div = document.getElementById(
        "selected-questions-list"
    );
    selected_questions_div.innerHTML = selected_questions_div.innerHTML.replace(
        "<p>" + id + "</p>",
        ""
    );

    // Remove selected class from question div
    let question_div = document.getElementById(id);
    if (question_div !== null) {
        question_div.classList.remove("selected");
    }

    // Show number of selected questions
    $("#sel-qns-h2").text(selected_questions.length + " Selected Question(s)");
}

// Populate selected questions div with selected questions from local storage
function populate_selected_questions() {
    // Get selected questions from local storage
    let selected_questions = JSON.parse(
        localStorage.getItem("selected_questions")
    );

    // If selected questions is not empty
    if (selected_questions !== null) {
        // For each selected question
        for (let i = 0; i < selected_questions.length; i++) {
            // Get question id
            let question_id = selected_questions[i];

            // Get question div
            let question_div = document.getElementById(question_id);

            // If question div exists
            if (question_div !== null) {
                // Add selected class to question div
                question_div.classList.add("selected");
            }

            // Add to selected questions div
            let selected_questions_div = document.getElementById(
                "selected-questions-list"
            );
            selected_questions_div.innerHTML += "<p>" + question_id + "</p>";
        }

        // Show number of selected questions
        $("#sel-qns-h2").text(selected_questions.length + " Selected Question(s)");
    } else {
        // Initialize selected questions array
        localStorage.setItem("selected_questions", JSON.stringify([]));
    }
}

// On page load, populate selected questions div
populate_selected_questions();

// When export to word button is pressed
document.getElementById("export-btn").addEventListener("click", function () {
    // Get selected questions from local storage
    let selected_questions = JSON.parse(
        localStorage.getItem("selected_questions")
    );

    // Reject if no questions are selected
    if (selected_questions === null || selected_questions.length === 0) {
        alert("Please select at least one question to export.");
        return;
    }

    // Create input element to store word document
    let input = document.createElement("input");
    input.type = "file";
    input.accept = ".docx";
    input.style.display = "none";
    input.click();

    // On file selected
    input.onchange = function () {
        // Get file
        let file = input.files[0];

        // Reject if file null
        if (file === null) {
            alert("Please select a word document to export to.");
            return;
        }

        // Create form data
        let formData = new FormData();
        formData.append("document", file);

        // Add list of questions to form data
        formData.append("questions", JSON.stringify(selected_questions));

        // Create request
        let request = new XMLHttpRequest();
        request.open("POST", "/api/question/export");
        request.send(formData);

        // On response
        request.onreadystatechange = function () {
            if (request.readyState !== 4) {
                return;
            }

            // If response is not ok
            if (request.status !== 200) {
                alert("Unable to export questions!\nError: " + request.responseText);
                return;
            }
        }
    }
});
