import DS from 'ember-data';
import USERFIXTURES from 'ember-gamers/fixtures/users';

var User = DS.Model.extend({
    username: DS.attr('string'),
    email: DS.attr('string'),
    first_name: DS.attr('string'),
    last_name: DS.attr('string')
});

User.reopenClass({
    FIXTURES: USERFIXTURES
});

export default User;
