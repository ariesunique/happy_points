const proxy = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(proxy('/points', { target: 'http://0.0.0.0:5000/' }));
};