function clearText(){
    document.getElementById("essay").value="";
}

function copyText() {
    const textArea = document.getElementById("essay");
    const text = textArea.value;

    if (text.trim() === "") {
        alert("Nothing to copy!");
        return;
    }

    navigator.clipboard.writeText(text)
        .then(() => {
            alert("Text copied to clipboard ✅");
        })
        .catch(err => {
            console.error("Failed to copy: ", err);
        });
}


// AJAX form submission
const form = document.querySelector("form");
form.addEventListener("submit", function(e){
    e.preventDefault();

    const essay = document.getElementById("essay").value;
    if(!essay.trim()) return alert ("Please enter some text!");

    fetch ("/predict", {
        method : "POST",
        body: new URLSearchParams({essay : essay})
    })
    .then(res => res.json())
    .then(data => {
        const box = document.getElementById("result");
        const text = document.getElementById("prediction-text");

        text.innerHTML = `<b>${data.prediction}</b><br>
            Confidence → Human: ${data.confidence_human}% | AI: ${data.confidence_ai}%<br>
            <b>Reason:</b> ${data.explanation.reason}<br>
            Avg Word Length: ${data.explanation.avg_word_len.toFixed(2)}<br>
            Vocabulary Richness: ${data.explanation.vocab_richness.toFixed(2)}<br>
            Stopword Ratio: ${data.explanation.stopword_ratio.toFixed(2)}`;

            box.className ="result-box " + (data.prediction === "Human Written" ? "success" : "danger");

            box.style.display = "block";
    })

    .ecatch(err => {console.error(err); alert("Prediction failed!");});

});