const express = require('express');

const app = express();
const port = process.env.PORT || 8080;

app.use(express.static(__dirname + '/public'));
80
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/frontend.html');
});

app.get('/backend', (req, res) => {
    res.sendFile(__dirname + '/backend.html');
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
