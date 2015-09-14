import DS from 'ember-data';
import GAMEFIXTURES from 'ember-gamers/fixtures/games';

var Game = DS.Model.extend({
    platform: DS.belongsTo('platform', {async: true}),
    slug: DS.attr('string'),
    title: DS.attr('string'),
    description: DS.attr('string'),
    publisher: DS.attr('string'),
    released: DS.attr('string'),
    rating: DS.attr('string'),
    added: DS.attr('string')
});

Game.reopenClass({
    FIXTURES: GAMEFIXTURES
});

export default Game;
