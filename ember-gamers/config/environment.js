/* jshint node: true */

module.exports = function(environment) {
  var ENV = {
    modulePrefix: 'ember-gamers',
    environment: environment,
    baseURL: '/',
    locationType: 'auto',
    EmberENV: {
      FEATURES: {
        // Here you can enable experimental features on an ember canary build
        // e.g. 'with-controller': true
      }
    },

    'simple-auth': {
        authorizer: 'simple-auth-authorizer:token'
    },
    'simple-auth-token': {
        tokenPropertyName: 'token',
        identificationField: 'username',
        refreshAccessTokens: true,
        timeFactor: 1000,
        refreshLeeway: 300, // Refresh the token 5 minutes (300s) before it expires.
    },
    APP: {
      // Here you can pass flags/options to your application instance
      // when it is created
    }
  };

  if (environment === 'development') {
      ENV.APP.API_HOST = 'http://localhost:8000';
      ENV.APP.API_NAMESPACE = 'api';
      ENV['simple-auth'].crossOriginWhitelist = [ENV.APP.API_HOST]

    // ENV.APP.LOG_RESOLVER = true;
    // ENV.APP.LOG_ACTIVE_GENERATION = true;
    // ENV.APP.LOG_TRANSITIONS = true;
    // ENV.APP.LOG_TRANSITIONS_INTERNAL = true;
    // ENV.APP.LOG_VIEW_LOOKUPS = true;
  }

  if (environment === 'test') {
    // Testem prefers this...
    ENV.baseURL = '/';
    ENV.locationType = 'none';

    // keep test console output quieter
    ENV.APP.LOG_ACTIVE_GENERATION = false;
    ENV.APP.LOG_VIEW_LOOKUPS = false;

    ENV.APP.rootElement = '#ember-testing';
  }

  if (environment === 'production') {

  }
  ENV['simple-auth-token'].serverTokenEndpoint = ENV.APP.API_HOST + '/api-token-auth/';
  ENV['simple-auth-token'].serverTokenRefreshEndpoint = ENV.APP.API_HOST + '/api-token-refresh/';
  ENV.contentSecurityPolicy = {
    'connect-src': "'self' " + ENV.APP.API_HOST,
    'style-src': "'self' fonts.googleapis.com 'unsafe-inline'",
    'font-src': "'self' fonts.gstatic.com"
  }
  return ENV;
};
