#!/usr/bin/node
// Prints message depending on argument length

if (process.argv.length === 2) {
    console.log('No argument');
}

else if (process.argv.length === 3) {
    console.log('Argument found');
}

else if (process.argv.length > 3) {
    console.log('Arguments found');
}
