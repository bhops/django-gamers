import Ember from 'ember';
import UnauthenticatedRouteMixin from 'simple-auth/mixins/unauthenticated-route-mixin';

export default Ember.Route.extend(UnauthenticatedRouteMixin, {
    setupController: function(controller) {
        controller.setProperties({
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': '',
            'password': '',
            'confirmpassword': ''
        });
    }
});
