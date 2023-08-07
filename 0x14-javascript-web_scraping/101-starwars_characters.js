#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  for (const c of characters) {
    request.get(c, (error, response, bodyc) => {
      if (error) {
        console.log(error);
      }

      const char = JSON.parse(bodyc);
      console.log(char.name);
    });
  }
});
