import DS from 'ember-data';
import PLATFORMFIXTURES from 'ember-gamers/fixtures/platforms';

var Platform = DS.Model.extend({
    name: DS.attr('string'),
    games: DS.hasMany('game', {async: true})
});

Platform.reopenClass({
    FIXTURES: PLATFORMFIXTURES
});

export default Platform;
