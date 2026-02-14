// static/script.js

document.getElementById('prediction-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const submitBtn = document.getElementById('submit-btn');
    const btnText = document.getElementById('btn-text');
    
    // UI Loading State
    const originalText = btnText.innerText;
    btnText.innerText = "Analyzing Building Data...";
    submitBtn.style.opacity = "0.7";
    submitBtn.style.pointerEvents = "none";

    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.heating) {
            document.getElementById('heating-val').innerText = result.heating;
            document.getElementById('cooling-val').innerText = result.cooling;
            document.getElementById('resultModal').style.display = 'flex';
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred during analysis.");
    } finally {
        // Reset Button
        btnText.innerText = originalText;
        submitBtn.style.opacity = "1";
        submitBtn.style.pointerEvents = "auto";
    }
});

function closeModal() {
    document.getElementById('resultModal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == document.getElementById('resultModal')) {
        closeModal();
    }
};