function openQuestionCreationForm() {
    var form = document.getElementById('create-question-form');
    form.style.display = "flex";
}

function closeQuestionCreationForm() {
    var form = document.getElementById('create-question-form');
    form.style.display = "none";
}

function submitSortingMethodForm(method) {
    document.getElementById("sorting-methods").submit();
    var radio = document.getElementById(method);
    radio.checked = true;

}