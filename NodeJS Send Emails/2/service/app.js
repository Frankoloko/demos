const express = require('express');
const app = express();

// To use req.body
    const bodyParser = require('body-parser');
    app.use(bodyParser.json());

// Morgan: to log every http call in the server console
    var morgan = require('morgan');
    app.use(morgan(':method :url [:date]'));

// Port & listen setup
    const port = 3000;
    const url = `http://200.0.0.140:${port}`;
    app.listen(port, () => console.log(`Listening on ${url} ...`));

// Pool: used for 'SELECT...' queries
    const { Pool } = require('pg');
    // './secrets/secrets' holds info like which database, which user to login with, which password etc.
    // you need to put this secrets.js in your git_ignore file (check udemy s5_36)
    const secrets = require('./secrets');
    const pool = new Pool(secrets);
    module.exports = pool;

// All your service routes
    const routes = require('./routes'); // ./routes is exporting 'app', we just assign it to 'routes' here to not overwrite our current app variable
    app.use('', routes); 
    // this empty '' is your default call url
    // for example '/feedback' will give you 'http://200.0.0.140:3000/feedback/testcall'
    // an empty string will give you 'http://200.0.0.140:3000/testcall'

// Error catcher
    // has to be AFTER other calls
    app.use((err, req, res, next) => {
        res.json(err);
    });
    // use example:
        // router.get('/feedback', (request, response, next) => {
        //     pool.query('SELECT * FROM "Client"', (err, res) => {
        //         if (err) return next(err);
        //         response.json(res.rows);
        //     });
        // });
