import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('users', function(){
      this.resource('user', { path: '/:username' });
  });
  this.route('signup');
  this.route('login');
  this.resource('platforms', function(){
    this.resource('platform', { path: '/:slug' });
  });
});

export default Router;
