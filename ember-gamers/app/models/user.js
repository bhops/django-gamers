import DS from 'ember-data';

export default DS.Model.extend({
    username: DS.attr('string'),
    password: DS.attr('string'),
    email: DS.attr('string'),
    first_name: DS.attr('string'),
    last_name: DS.attr('string'),
    dob: DS.attr('date'),
    about: DS.attr('string'),
    sex: DS.attr('string')
});
