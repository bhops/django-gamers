import DS from 'ember-data';

export default DS.Model.extend({
    username: DS.attr('string'),
    first_name: DS.attr('string'),
    last_name: DS.attr('string'),
    dob: DS.attr('string'),
    about: DS.attr('string'),
    sex: DS.attr('string')
});
