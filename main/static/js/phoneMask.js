const inputs = document.querySelectorAll("input[type='tel']");

inputs.forEach(input => {
    input.addEventListener('input', (e) => {
        if(input.value.length > 18) input.value = input.value.slice(0, 18);
        if(e.inputType !== "deleteContentBackward") {
            input.value = input.value
            .replace(/\D/g, "")
            .replace(/^(\d{1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/, "+$1 ($2) $3-$4-$5");
        }else {
            input.value = input.value.slice(0, input.value.length)
        }
    })
})