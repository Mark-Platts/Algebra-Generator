//const mainURL = 'https://cors-anywhere.herokuapp.com/https://api.datamuse.com/words';
const mainURL = 'http://markplatts.co.uk/equation-api'; //live
//const mainURL = 'http://localhost:5000/'; //test

//const testObj = {"values": [-4, 0, 28, -8, -9, -8], "answer": "9", "solution": " -4x + 28 \n\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 - 9 = -8\n -8 \n\nTake -9 to the right hand side.\n -4x + 28 \n\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 = 1\n -8 \n\nMultiply both sides by the denominator.\n-4x + 28 = 1(-8)\n\nMultiply out the brackets. \n-4x + 28 = -8\n\nTake 28 to the right hand side.\n-4x = -36\n\nDivide by -4.\nx = 9\n\nDone!", "display": " -4x + 28 \n\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500 - 9 = -8\n -8 "}
const testObj = {"display": "<p> \( -4x + 28 \over - 9 = -8\n -8 \) </p>"}


function search() {
    const level1 = document.getElementById("level1").checked;
    const level2 = document.getElementById("level2").checked;
    const level3 = document.getElementById("level3").checked;
    const level4 = document.getElementById("level4").checked;
    const level5 = document.getElementById("level5").checked;
    let queryBase = 1;

    if (level1) {
        queryBase = '/1';
    }
    else if (level2) {
        queryBase = '/2';
    }
    else if (level3) {
        queryBase = '/3';
    }
    else if (level4) {
        queryBase = '/4';
    }
    else if (level5) {
        queryBase = '/5';
    }
    
    const endpoint = mainURL + queryBase;

    const results = getResult(endpoint);
    //renderResults(results)
}

async function getResult(endpoint) {
    renderResults(testObj)
    /* try {
        const response = await fetch(endpoint, { cache: 'no-cache'});
        if (response.ok) {
            console.log(response)
            //const jsonResponse = await response.json();
            //renderResults(jsonResponse);
            return
        }
        throw new Error('Request Failed!');
    } catch(error) {
        console.log(error);
    } */
}

function renderResults(results) {
    let display = results.display;
    let hold = '<center><br>';
    for (let i = 0; i < results.length; i++) {
        const word = results[i]["word"];
        hold += word+'<br>';
    }
    hold += '<br></center>';
    document.getElementById("result").innerHTML = display;
    MathJax.Hub.Queue(["Typeset",MathJax.Hub,"result"]);
}
