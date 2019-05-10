// let num1 = parseInt(prompt('Input a number'));
// let num2 = parseInt(prompt('Input a number'));
// let num3 = parseInt(prompt('Input a number'));
// let num4 = parseInt(prompt('Input a number'));


// function averagenum(num1, num2, num3, num4) {
//     let avg = (num1 + num2 + num3 + num4) / 4;
//     return avg
// }

// avg = averagenum(num1, num2, num3, num4);

function createNumArray(){
    numArray = [];
    answer = ''
    while(answer != 'done') {
        answer = prompt('Input a number or "done"');
        if (answer != 'done') {
            numArray.push(answer)
        }
    }
    return numArray
}

function averageNumArray(inputArray) {
    let total = 0;
    for (let i = 0; i < inputArray.length; i++) {
     total += parseInt(inputArray[i]);
    }   
    let av = (total / inputArray.length);
    return av
}

let numberList = createNumArray();
let avg = averageNumArray(numberList);


console.log(numberList);
console.log(avg);
