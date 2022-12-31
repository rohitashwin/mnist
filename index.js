const express = require('express');
const fs = require('fs/promises');
const { spawn, exec } = require('child_process');
const dotenv = require('dotenv');

dotenv.config();
const app = express();

app.use(express.static('public'));
app.use(express.json());

app.post('/predict', async (req, res) => {
	console.log('predicting');
	// get the 28x28 image from the body
	const image = req.body.image;
	// write the json content to a file
	await fs.writeFile('image.json', JSON.stringify(image));
	console.log('Writing image to file');
	// spawn a python process to run the prediction
	const python = exec('python3 ./python/main.py --predict --image image.json --model ./python/model.pth', (err, stdout, stderr) => {
		if (err) {
			console.log(err);
			return;
		} else if (stderr) {
			console.log(stderr);
			return;
		}
		console.log(stdout);
		res.send(JSON.stringify(stdout));
		console.log(stdout);
	});
});

const PORT = process.env.PORT || 8080;

app.listen(PORT, () => {
	  console.log(`Server listening on port ${PORT}...`);
});