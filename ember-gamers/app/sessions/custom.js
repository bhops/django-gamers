import Ember from 'ember';
import DS from 'ember-data';
import Session from 'simple-auth/session';

export default Session.extend({
    currentUser: function() {
        var username = this.get('secure.username');
        if (!Ember.isEmpty(username)) {
            return DS.PromiseObject.create({
                promise: this.container.lookup('store:main').find('user', username)
            });
        }
    }.property('secure.user_id')
});
