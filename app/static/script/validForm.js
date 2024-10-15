
// TODO: A modifier les valeurs mais pour le test tous seras mis à 50 max
const maxLenght = 20;
const minLenght = 4;

function checkValidInput(element, data) {

    let input = document.getElementById(element);
    const helper = document.getElementById(element + 'Help');

    if (data.length > minLenght && data.length < maxLenght) {
        input.setAttribute('class', 'form-control form-control-sm is-valid');
        // Change le message d'aide
        helper.setAttribute('class', 'text-start valid-feedback');
        helper.innerHTML = "";
    }
    else {
        input.setAttribute('class', 'form-control form-control-sm is-invalid')
        // Change le message d'aide
        helper.setAttribute('class', 'text-start invalid-feedback');
        helper.innerHTML = "Minimum " + minLenght + " caractères et" + maxLenght + "maximum.";
    }
}