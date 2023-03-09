// On select div, add a selected class to the selected option
function on_select(id) {
    let question_div = document.getElementById(id);

    // If the div is already selected, deselect it and vice-versa
    if (question_div.classList.contains("selected")) {
        question_div.classList.remove("selected");
    } else {
        question_div.classList.add("selected");
    }
}

// Make function global
window.on_select = on_select;

// On delete button click, ask for confirmation and delete selected questions
function on_delete(id) {
    if (confirm("Are you sure you want to delete this question?\nAction is irreversible!") === true) {
        location.href = "/api/question/delete?id=" + id;
    }
}

// Make function global
window.on_delete = on_delete;

// On search button click, search for questions
document.getElementById("search-btn").addEventListener("click", function() {
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
$("#section-select").chosen({width: "50px"});
$("#category-select").chosen();
