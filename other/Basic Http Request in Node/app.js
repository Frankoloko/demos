const http = require('request');

const postBody = {
    "something": "some value"
}

http.post({headers: {'content-type': 'application/json'}, url: 'http://x/someCall', body: JSON.stringify(postBody)},
(err, res, body) => {    
    if (err) return console.log(err);

    console.log(body);
});

http.get('http://x/someCall', (err, res, body) => {
    if (err) return console.log(err);

    console.log(body);
});