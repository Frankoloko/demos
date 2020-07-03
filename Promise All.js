async function run() {
    const arrPromises = [];

    arrPromises.push(new Promise(resolve => {
        setTimeout(() => {
            console.log('1 done');
            resolve()
        }, 3000);
    }));
    
    arrPromises.push(new Promise(resolve => {
        setTimeout(() => {
            console.log('2 done');
            resolve()
        }, 5000);
    }));
    
    await Promise.all(arrPromises);
    console.log('done with all');
};

run();

// Will log
    // 1 done
    // 2 done
    // done with all