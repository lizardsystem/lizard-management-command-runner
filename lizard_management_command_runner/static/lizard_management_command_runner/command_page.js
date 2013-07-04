$("button.commandrunner").click(function () {
    var command_url = $(this).attr("data-command-url");

    $.post(command_url);
});

$("a.toggle-visibility").click(function (event) {
    var $a = $(this);
    var $span = $("#" + $a.attr("data-span-id"));

    if ($span.attr("data-visible") === "0") {
        $span.css("display", "block");
        $span.attr("data-visible", "1");
        $a.text('verberg output');
    } else {
        $span.css("display", "none");
        $span.attr("data-visible", "0");
        $a.text("toon output");
    }
    event.preventDefault();
});
