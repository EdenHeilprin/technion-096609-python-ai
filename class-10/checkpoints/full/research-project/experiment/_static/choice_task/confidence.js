// Find the existing confidence radios and the text displayed underneath them.
const confidenceRadios = document.querySelectorAll('input[name="confidence"]');
const confidencePreview = document.getElementById('confidence-preview');

function showConfidence() {
    // Read whichever radio is selected; do not select a default for the participant.
    const selected = document.querySelector('input[name="confidence"]:checked');
    confidencePreview.textContent = selected
        ? `Your confidence: ${selected.value} out of 7`
        : 'Choose a confidence rating';
}

// Update the preview whenever the participant changes their selection.
for (const radio of confidenceRadios) {
    radio.addEventListener('change', showConfidence);
}

// oTree may restore unfinished inputs when the page is loaded again.
window.addEventListener('load', showConfidence);
window.addEventListener('pageshow', showConfidence);
