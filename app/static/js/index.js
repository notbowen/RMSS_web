// EditorJS
const editor_question = new EditorJS({
    holder: "editorjs_question",
    placeholder: "Enter question content here...",
    tools: {
        paragraph: {
            class: Paragraph,
            inlineToolbar: ["bold", "italic"],
        },
        list: {
            class: List,
            inlineToolbar: true,
        },
        table: {
            class: Table,
            inlineToolbar: true,
        },
        image: {
            class: ImageTool,
            config: {
                endpoints: {
                    byFile: "/api/image/upload_file",
                    byUrl: "/api/image/upload_url",
                },
            },
            inlineToolbar: true,
        },
    },
});

// EditorJS for answer
const editor_answer = new EditorJS({
    holder: "editorjs_answer",
    placeholder: "Enter answer here...",
    minHeight: 100,
    tools: {
        paragraph: {
            class: Paragraph,
            inlineToolbar: ["bold", "italic"],
        },
        list: {
            class: List,
            inlineToolbar: true,
        },
        table: {
            class: Table,
            inlineToolbar: true,
        },
    },
});

// Alert user if EditorJS fails to load
editor_question.isReady
    .then(() => {
        console.log("EditorJS is ready to work!");
    })
    .catch((reason) => {
        console.log("EditorJS initialization failed because of ", reason);
    });

editor_answer.isReady
    .then(() => {
        console.log("EditorJS is ready to work!");
    })
    .catch((reason) => {
        console.log("EditorJS initialization failed because of ", reason);
    });

// Hook save button to EditorJS
document.getElementById("save-btn").addEventListener("click", async () => {
    // Initialise JSON response
    let response = {};

    // Get data from EditorJS
    await editor_question
        .save()
        .then((outputData) => {
            response["content"] = outputData;
        })
        .catch((error) => {
            console.log("Saving failed: ", error);
            return;
        });

    // Get answer from EditorJS
    await editor_answer
        .save()
        .then((outputData) => {
            response["answer"] = outputData;
        })
        .catch((error) => {
            console.log("Saving failed: ", error);
            return;
        });

    // Get selected question type
    let question_type_select = document.getElementById("qn-section");
    response["section"] =
        question_type_select.options[question_type_select.selectedIndex].value;

    // Get question id and add to response
    if (validateQuestionID()) {
        let question_id = "";
        question_id +=
            document.getElementById("qn-school").value.trim().toUpperCase() +
            "-";
        question_id += document.getElementById("qn-level").value.trim() + "-";
        question_id +=
            document.getElementById("qn-test").value.trim().toUpperCase() + "-";
        question_id += document.getElementById("qn-year").value.trim() + "-";
        question_id += document.getElementById("qn-section").value.trim() + "-";
        question_id += document.getElementById("qn-number").value.trim();
        response["id"] = question_id;
    } else {
        alert("Ensure that all question ID fields are valid!");
        return;
    }

    // Get question category
    let question_category_select = document.getElementById("qn-category");
    let selected =
        question_category_select.options[question_category_select.selectedIndex]
            .value;
    response["category_id"] = selected;

    // Debug
    console.log(response);

    // Prepare to send data as a POST request to the server
    var xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    xhr.open("POST", "/api/question/save", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
        // Alert user if save failed
        if (xhr.readyState === 4 && xhr.status !== 200) {
            try {
                alert(
                    "Failed to save question!\nError: " +
                        xhr.response["message"]
                );
            } catch (error) {
                alert("Error connecting to server! Please try again later.");
            }
        }

        // Alert user if save succeeded
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert("Question saved successfully!");

            // Clear editor and answer
            editor_question.clear();
            editor_answer.clear();
        }
    };

    // Send data to server
    xhr.send(JSON.stringify(response));
});

// Ensure that question id fields are not empty
function validateQuestionID() {
    return !(
        document.getElementById("qn-school").value.trim() === "" ||
        document.getElementById("qn-level").value.trim() === "" ||
        document.getElementById("qn-test").value.trim() === "" ||
        document.getElementById("qn-year").value.trim() === "" ||
        document.getElementById("qn-number").value.trim() === ""
    );
}

// Add filtering to question type and category select
$("#qn-category").chosen({
    no_results_text: "No results matched",
    width: "394px",
});
$("#qn-level").chosen({ no_results_text: "No results matched" });
$("#qn-section").chosen({
    no_results_text: "No results matched",
    width: "50px",
});
