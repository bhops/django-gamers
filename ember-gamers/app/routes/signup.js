import Ember from 'ember';
import UnauthenticatedRouteMixin from 'simple-auth/mixins/unauthenticated-route-mixin';

export default Ember.Route.extend(UnauthenticatedRouteMixin, {
    setupController: function(controller) {
        controller.setProperties({
            'firstname': '',
            'lastname': '',
            'dob': '',
            'sex': '',
            'username': '',
            'email': '',
            'password': '',
            'confirmpassword': ''
        });
    }
});
