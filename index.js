const protect = require('static-auth');
const safeCompare = require('safe-compare');

/*
 *
 */

const app = protect(
  '/admin',
  (username, password) => safeCompare(username, 'yuki') && safeCompare(password, '060415'),
  {
    directory: __dirname + '/_static',
    realm: 'vercel-basic-auth.node-static-auth',
    onAuthFailed: res => {
      res.end('Authentication failure');
    }
  }
);

module.exports = app;
