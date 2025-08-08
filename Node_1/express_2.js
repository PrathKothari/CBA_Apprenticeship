const express = require('express');
const path = require('path');
const app = express();
const port = 8080;

// ✅ Set the view engine and views directory
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// ✅ Route to render the template
app.get('/', (req, res) => {
  const name = req.query.name || 'Guest';  // Get name from URL query (?name=YourName)

  const data = {
    title: 'Express Template Example',
    message: `Hello, ${name}!`,
    items: ['Apple', 'Mango', 'Banana']
  };

  res.render('index', data);
});

// ✅ Start the server
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
