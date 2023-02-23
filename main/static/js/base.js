function openQuestionCreationForm() {
    var form = document.getElementById('create-question-form');
    form.style.display = "flex";
}

function closeQuestionCreationForm() {
    var form = document.getElementById('create-question-form');
    form.style.display = "none";
}

function submitSortingMethodForm() {
    document.getElementById("sorting-methods").submit()
}