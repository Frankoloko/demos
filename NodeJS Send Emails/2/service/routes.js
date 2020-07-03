// Setup
    const express = require('express');
    const app = express();
    module.exports = app;
    const pool = require('./app');

// Extra Functions
    splitObject = (pPath, pMethod, pObject) => {
        // Split object into arrays
            let keys = [];
            const values = [];
            const placeholders = [];
            let i = 0;
            
            for (var key in pObject) {
                if (key.toLocaleLowerCase() == 'uuid') continue;
                keys.push(`"${key}"`);
                values.push(pObject[key]);
                i++;
                placeholders.push(`$${i}`);
            }

        // INSERT
            if (pMethod.toLocaleLowerCase() == 'insert') {
                return {
                    query: `INSERT INTO "${pPath}" (${keys}) VALUES (${placeholders})`,
                    values: values
                }
            }

        // UPDATE
            if (pMethod.toLocaleLowerCase() == 'update') {
                keys = keys.map((element, index) => {return `${element}=(${placeholders[index]})`});
                return {
                    query: `UPDATE "${pPath}" SET ${keys.join(',')} WHERE "UUID"='${pObject.UUID}'`,
                    values: values
                }
            }
    }

// Create REST calls (db prefix)
    createRESTCalls = (pPath) => {
        restCallsPrefix = 'db';

        app.get(`/${restCallsPrefix}${pPath}`, (request, response, next) => {
            pool.query(`SELECT * FROM "${pPath}"`, (err, res) => {
                if (err) return next(err);
                response.json(res.rows);
            });
        });

        app.post(`/${restCallsPrefix}${pPath}`, (request, response, next) => {
            const obj = splitObject(pPath, 'INSERT', request.body);
            pool.query(obj.query, obj.values, (err, res) => {
                if (err) return next(err);
                response.json(res);
            });
        });

        app.put(`/${restCallsPrefix}${pPath}`, (request, response, next) => {
            const obj = splitObject(pPath, 'UPDATE', request.body);
            pool.query(obj.query, obj.values, (err, res) => {
                if (err) return next(err);
                response.json(res);
            });
        });

        app.delete(`/${restCallsPrefix}${pPath}`, (request, response, next) => {
            pool.query(`DELETE FROM "${pPath}" WHERE "UUID"=($1)`, [request.query.UUID], (err, res) => {
                if (err) return next(err);
                response.json(res);
            });
        });
    }

    // These names need to be EXACTLY the same as the database table names
    createRESTCalls('Client');
    createRESTCalls('ClientProduct');
    createRESTCalls('Feedback');
    createRESTCalls('Product');
    createRESTCalls('Progress');
    createRESTCalls('Staff');
    createRESTCalls('TeamMember');
    createRESTCalls('User');

// Function Calls (ut prefix)
    app.get('/utGetFeedbackTypeOptions', (request, response, next) => {
        pool.query('SELECT "FeedbackTypeOptions" FROM "Product" WHERE "UUID"=($1)', [request.query.UUID], (err, res) => {
            if (err) return next(err);
            response.json(res.rows[0]['FeedbackTypeOptions']);
        });
    })
