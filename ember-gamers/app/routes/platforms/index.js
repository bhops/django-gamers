import Ember from 'ember';

export default Ember.Route.extend({
    model: function() {
        return Ember.RSVP.hash({
            platforms: this.store.findAll('platform'),
            games: this.store.findAll('game')
        });
    },
    setupController: function(controller, model){
        controller.set('model.platforms', model.platforms);
        controller.set('model.games', model.games);
    }
});
