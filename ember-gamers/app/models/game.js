import DS from 'ember-data';

export default DS.Model.extend({
    platform: DS.belongsTo('platform', {embedded: 'always'}),
    slug: DS.attr('string'),
    title: DS.attr('string'),
    description: DS.attr('string'),
    publisher: DS.attr('string'),
    released: DS.attr('string'),
    rating: DS.attr('string'),
    added: DS.attr('string')
});
