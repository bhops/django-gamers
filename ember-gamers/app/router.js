import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('users', function(){
      this.resource('user', { path: '/:user_id' })
  });
  this.route('users', function() {});
});

export default Router;
