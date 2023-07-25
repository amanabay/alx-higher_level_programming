#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  const movies = data.results.filter((movie) => {
    return movie.characters.filter((url) => {
      return url.includes(18);
    }).length;
  });

  console.log(movies.length);
});
