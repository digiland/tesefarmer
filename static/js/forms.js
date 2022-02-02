
const imageForm = document.getElementsByClassName("image-form");
console.log(imageForm);
const mainForm = document.querySelector("#post_form");

const addImageFormBtn = document.querySelector("#add-image-form");
const submitFormBtn = document.querySelector('[type="submit"]');

const totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formCount = imageForm.length - 1;

function updateForms() {
    let count = 0;
    for (let form of imageForm) {
        const formRegex = RegExp(`form-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `form-${count++}-`)
    }
}

addImageFormBtn.addEventListener("click", function (event) {
    event.preventDefault();

    const newImageForm = imageForm[0].cloneNode(true);
    const formRegex = RegExp(`form-(\\d){1}-`, 'g');
    console.log("We are here")
    formCount++;

    newImageForm.innerHTML = newImageForm.innerHTML.replace(formRegex, `form-${formCount}-`);
    mainForm.insertBefore(newImageForm, submitFormBtn);
    totalForms.setAttribute('value', `${formCount + 1}`);
});

mainForm.addEventListener("click", function (event) {
    if (event.target.classList.contains("delete-image-form")) {
        event.preventDefault();
        event.target.parentElement.remove();
        formCount--;
        updateForms();
        totalForms.setAttribute('value', `${formCount + 1}`);
    }
});