// Detect enter key press function
$.fn.enterKey = function (fnc) {
    return this.each(function () {
        $(this).keypress(function (ev) {
            var keycode = (ev.keyCode ? ev.keyCode : ev.which);
            if (keycode == '13') {
                fnc.call(this, ev);
            }
        })
    })
}

// Main
$(document).ready(function($) {
    // Hide the save and cancel buttons
    $(document).find(".btn_save").hide();
    $(document).find(".btn_cancel").hide();

    // Make whole table row editable
    $(document).on("click", ".btn_edit", function(event) {
        event.preventDefault();
        var tbl_row = $(this).closest("tr");

        tbl_row.find(".btn_save").show();
        tbl_row.find(".btn_cancel").show();

        tbl_row.find(".btn_edit").hide();

        // Make whole row editable
        tbl_row.find(".row_data")
            .attr("contenteditable", "true")
            .attr("edit_type", "button")
            .addClass("bg-warning")
            .css("padding", "3px");

        // Backup original entry
        tbl_row.find(".row_data").each(function(index, val) {
            $(this).attr("original_entry", $(this).html());
        });
    });

    // On user click cancel
    $(document).on("click", ".btn_cancel", function(event) {
        event.preventDefault();
        var tbl_row = $(this).closest("tr");

        // Hide save & cancel buttons
        tbl_row.find(".btn_save").hide();
        tbl_row.find(".btn_cancel").hide();

        // Show edit button
        tbl_row.find(".btn_edit").show();

        // Make the whole row uneditable
        tbl_row.find(".row_data")
            .attr("contenteditable", "false")
            .attr("edit_type", "click")
            .removeClass("bg-warning")
            .css("padding", "");

        // Restore original data
        tbl_row.find(".row_data").each(function(index, val) {
            $(this).html($(this).attr("original_entry"));
        });
    });

    // Save whole table row entry
    $(document).on("click", ".btn_save", function(event) {
        event.preventDefault();

        var tbl_row = $(this).closest("tr");
        var row_id = tbl_row.attr("row_id");

        // Hide save & cancel buttons
        tbl_row.find(".btn_save").hide();
        tbl_row.find(".btn_cancel").hide();

        // Show edit button
        tbl_row.find(".btn_edit").show();

        // Make the whole row uneditable
        tbl_row.find(".row_data")
            .attr("contenteditable", "false")
            .attr("edit_type", "click")
            .removeClass("bg-warning")
            .css("padding", "");

        // Get row data
        var arr = {};
        tbl_row.find(".row_data").each(function(index, val) {
            var col_name = $(this).attr("col_name");
            var col_val = $(this).text();

            arr[col_name] = col_val;
        });

        // Send to server
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/topics/edit?id=" + row_id, true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status !== 200) {
                alert("Failed to edit topic!\nError: " + xhr.responseText);
            }
        }

        xhr.send(JSON.stringify(arr));
    });

    // Lose focus when user presses enter
    $(".row_data").enterKey(function() {
        $(".row_data").blur();
    });

    // Add new topic
    $("#btn_add_topic").click(function(event) {
        var level = $("#level").val();
        var topic = $("#topic").val();
        var subject = $("#subject").val();

        if (level.trim() == "" || topic.trim() == "" || subject.trim() == "") {
            alert("Please fill in all fields!");
            return;
        }

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/topics/add", true);
        xhr.setRequestHeader("Content-Type", "application/json");

        xhr.onreadystatechange = function() {
            if (xhr.readyState !== 4) return;

            if (xhr.status !== 200) {
                alert("Failed to add topic!\nError: " + xhr.responseText);
                return;
            }

            // Clear fields
            $("#level").val("");
            $("#topic").val("");
            $("#subject").val("");

            // Reload page
            location.reload();
        }

        xhr.send(JSON.stringify({
            "level": level,
            "topic": topic,
            "subject": subject
        }));
    });
});