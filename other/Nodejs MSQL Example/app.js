// Setup Data
    // To write calls
        const express = require('express');
        const app = express();
        const port = 2109;
        app.listen(port, function () {
            console.log(`Server is running on port: ${port}`);
        });

    // To use request.body
        const bodyParser = require('body-parser');
        app.use(bodyParser.json());

    // MSSQL
        // If you run into errors, check these:
        // To get config.port: https://stackoverflow.com/questions/12297475/how-to-find-sql-server-running-port
        // Enable the connection: https://stackoverflow.com/questions/25577248/node-js-mssql-tedius-connectionerror-failed-to-connect-to-localhost1433-conn
        const sql = require('mssql');
        var config = {
            user: 'Admin',
            password: 'admin',
            server: 'x', 
            database: 'x',
            port: x
        };
        var connection;
        sql.connect(config, () => {
            connection = new sql.Request();
        });

// Calls
    app.get('/test', (request, response) => {
        // connection.query(`SELECT * FROM Trips`, (err, result) => {
        connection.query(`SELECT * FROM [dbo].[TripList] where pickUpDate >= '2017-01-01' and pickUpDate <= '2018-01-01'`, (err, result) => {
        // connection.query(`SELECT * FROM Client`, (err, result) => {
            if (err) return response.status(200).send(err);
            response.status(200).send(result);
        });

        // To get the body from a POST use 'request.body'
    });