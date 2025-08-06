const https = require('https');

https.get('https://jsonplaceholder.typicode.com/posts/2', (res) => {
  let data = '';

  res.on('data', chunk => data += chunk);
  res.on('end', () => {
    const post = JSON.parse(data);
    console.log("Title:", post.title);
  });
}).on('error', err => console.error('Error:', err.message));