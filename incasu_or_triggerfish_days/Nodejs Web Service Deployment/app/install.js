var config = require('../config');
var Service = require('node-windows').Service;

// Create a new service object
    var svc = new Service({
        name: config.name,
        description: config.description,
        script: config.script,
        nodeOptions: [
            '--harmony',
            '--max_old_space_size=4096'
        ]
    });

// Install
    svc.on('install', function () {
        svc.start();
    });
    svc.install();