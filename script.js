
document.getElementById('cropForm').addEventListener('submit', async function(e) {
  e.preventDefault();
  const formData = new FormData(this);
  const data = Object.fromEntries(formData);
  const response = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });
  const result = await response.json();
  document.getElementById('result').innerText = 'Predicted Yield: ' + result.yield + ' quintals/ha';
});
