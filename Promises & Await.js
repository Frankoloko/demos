//##################################################################
function SonderPromises() {
    console.log("One: Started");
    setTimeout(function(){console.log("One: Completed")}, 1000);
    console.log("Two: Started");
    setTimeout(function(){console.log("Two: Completed")}, 2000);
    console.log("Three: Started");
    setTimeout(function(){console.log("Three: Completed")}, 3000);
}
//##################################################################
async function MetPromises() {
    console.log("One: Started");
    await (function() {
        return new Promise((resolve, reject) => {
            setTimeout(function(){
                console.log("One: Completed");
                resolve();
            }, 1000);
        });
    })();
    console.log("Two: Started");
    await (function() {
        return new Promise((resolve, reject) => {
            setTimeout(function(){
                console.log("Two: Completed");
                resolve();
            }, 1000);
        });
    })();
    console.log("Three: Started");
    await (function() {
        return new Promise((resolve, reject) => {
            setTimeout(function(){
                console.log("Three: Completed");
                resolve();
            }, 1000);
        });
    })();
}
//##################################################################
async function MetPromises_SonderNamelessFunksie() {
    console.log("One: Started");
    await new Promise((resolve, reject) => {
        setTimeout(function(){
            console.log("One: Completed");
            resolve();
        }, 1000);
    });
    console.log("Two: Started");
    await new Promise((resolve, reject) => {
        setTimeout(function(){
            console.log("Two: Completed");
            resolve();
        }, 1000);
    });
    console.log("Three: Started");
    await new Promise((resolve, reject) => {
        setTimeout(function(){
            console.log("Three: Completed");
            resolve();
        }, 1000);
    });
}
//##################################################################
function SonderAsync() {
    console.log("One: Started");
    let MyPromise1 = new Promise((resolve, reject) => {
        setTimeout(function(){
            console.log("One: Completed");
            resolve();
        }, 1000);
    }).then(()=>{
        console.log("Two: Started");
        let MyPromise2 = new Promise((resolve, reject) => {
            setTimeout(function(){
                console.log("Two: Completed");
                resolve();
            }, 1000);
        }).then(()=>{
            console.log("Three: Started");
            let MyPromise3 = new Promise((resolve, reject) => {
                setTimeout(function(){
                    console.log("Three: Completed");
                    resolve();
                }, 1000);
            });
        })
    })
}
//##################################################################
function HttpCall() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('done');
        }, 3000);
    })
}

async function WaarJyDitSalWilGebruik() {
    console.log('begin call');
    console.log(await HttpCall());
    console.log('call klaar');
}

//SonderPromises();
//MetPromises();
//MetPromises_SonderNamelessFunksie();
//SonderAsync()
WaarJyDitSalWilGebruik();