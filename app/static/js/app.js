// EditorJS
const editor = new EditorJS({
    holder: "editorjs",
    tools: {
        paragraph: {
            class: Paragraph,
            inlineToolbar: true,
        },
        list: {
            class: List,
            inlineToolbar: [
                "link",
                "bold"
            ],
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
                }
            },
            inlineToolbar: true,
        }
    },
});

// Alert if EditorJS fails to load
try {
    await editor.isReady;
    console.log("Editor.js is ready!");
} catch (error) {
    alert("Editor.js initialisation failed due to " + error);
}

// Hook save button to EditorJS
document.getElementById("save-btn").addEventListener("click", async () => {
    // Initialise JSON response
    let response = {};

    // Get data from EditorJS
    await editor.save().then((data) => {
        response["editorjs"] = data;
    }).catch((error) => {
        alert("Saving failed: " + error);
        return;
    });

    // Get question id and add to response
    let question_id = document.getElementById("question-id").value;
    response["question_id"] = question_id;

    // Get selected question type
    let question_type_select = document.getElementById("qn-type");
    let selected = question_type_select.options[question_type_select.selectedIndex].text;
    response["question_type"] = selected;

    // Get answer
    let answer = document.getElementById("answer").value;
    response["answer"] = answer;

    // Debug
    console.log(response);

    // Prepare to send data as a POST request to the server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/api/question/save", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    // Alert user if error occurs
    xhr.onreadystatechange = function () {
        if (!(xhr.readyState === 4 && xhr.status === 200)) {
            alert("Error while saving question!");
            return;
        } 
    };

    // Send data to server
    xhr.send(JSON.stringify(response));
});

// Hook editing toggle button to EditorJS
document.getElementById("edit-btn").addEventListener("click", () => {
    editor.isReady.then(() => {
        editor.readOnly.toggle();
        if (editor.readOnly.isEnabled) {
            document.getElementById("edit-btn").innerHTML = "<i class='fa fa-lock'></i>"
        } else {
            document.getElementById("edit-btn").innerHTML = "<i class='fa fa-unlock'></i>"
        }
    });
});