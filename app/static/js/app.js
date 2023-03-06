// EditorJS
const editor = new EditorJS({
  holder: "editorjs",
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
  await editor
    .save()
    .then((outputData) => {
      response["content"] = outputData;
    })
    .catch((error) => {
      console.log("Saving failed: ", error);
      return;
    });

  // Get selected question type
  let question_type_select = document.getElementById("qn-section");
  let selected =
    question_type_select.options[question_type_select.selectedIndex].value;
  response["is_mcq"] = selected === "A";

  // Get question id and add to response
  if (validateQuestionID()) {
    let question_id = "";
    question_id +=
      document.getElementById("qn-school").value.trim().toUpperCase() + "-";
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
  selected =
    question_category_select.options[question_category_select.selectedIndex]
      .value;
  response["category_id"] = selected;

  // Get answer
  let answer = document.getElementById("answer").value;
  response["answer"] = answer;

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
        alert("Failed to save question!\nError: " + xhr.response["message"]);
      } catch (error) {
        alert("Error connecting to server! Please try again later.");
      }
    }
  };

  // Send data to server
  xhr.send(JSON.stringify(response));
});

// Hook editing toggle button to EditorJS
// document.getElementById("edit-btn").addEventListener("click", () => {
//     // Toggle read-only mode
//     editor.readOnly.toggle();
//
//     // Change button icon accordingly
//     if (editor.readOnly.isEnabled) {
//         document.getElementById("edit-btn").innerHTML = "<i class='fa fa-lock'></i>"
//     } else {
//         document.getElementById("edit-btn").innerHTML = "<i class='fa fa-unlock'></i>"
//     }
// });

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
