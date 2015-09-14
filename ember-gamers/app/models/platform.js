import DS from 'ember-data';
import PLATFORMFIXTURES from 'ember-gamers/fixtures/platforms';

var Platform = DS.Model.extend({
    name: DS.attr('string'),
    games: DS.hasMany('game', {async: false}),

    numGames: function() {
        return this.get('games').get('length');
    }.property('games')
});

Platform.reopenClass({
    FIXTURES: PLATFORMFIXTURES
});

export default Platform;
