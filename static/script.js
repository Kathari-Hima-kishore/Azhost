document.getElementById('sendBtn').addEventListener('click', async () => {
    const resultEl = document.getElementById('result');
    resultEl.textContent = 'Sending...';
    try {
        const response = await fetch('/send-message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: 'Hello from the cool site!' })
        });
        const data = await response.json();
        resultEl.textContent = JSON.stringify(data, null, 2);
    } catch (e) {
        resultEl.textContent = 'Error: ' + e;
    }
});

document.getElementById('getOneBtn').addEventListener('click', async () => {
    const resultEl = document.getElementById('result');
    resultEl.textContent = 'Getting One...';
    try {
        const response = await fetch('/get-message/one');
        const data = await response.json();
        resultEl.textContent = JSON.stringify(data, null, 2);
    } catch (e) {
        resultEl.textContent = 'Error: ' + e;
    }
});

document.getElementById('getTwoBtn').addEventListener('click', async () => {
    const resultEl = document.getElementById('result');
    resultEl.textContent = 'Getting Two...';
    try {
        const response = await fetch('/get-message/two');
        const data = await response.json();
        resultEl.textContent = JSON.stringify(data, null, 2);
    } catch (e) {
        resultEl.textContent = 'Error: ' + e;
    }
});
