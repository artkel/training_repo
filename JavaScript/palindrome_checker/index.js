const input = document.getElementById("input")

function check() {
    const value = input.value;
    const reversedValue = value.split('').reverse().join('').toLowerCase();
    
    if (value.toLowerCase() === reversedValue) {
        alert(`${value} is a palindrome`)
    } else {
        alert(`${value} is not a palindrome`)
    }
}