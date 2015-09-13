import Ember from 'ember';

export default Ember.Controller.extend({
    first_name: '',
    last_name: '',
    username: '',
    email: '',
    password: '',
    confirmpassword: '',
    actions: {
        signup: function() {
            var self = this;
            if (self.get('password') === self.get('cpassword')) {
                return $.ajax({
                    url: 'http://localhost:8000/api/users/',
                    type: 'POST',
                    crossDomain: true,
                    data: self.getProperties('first_name', 'last_name',
                                             'username', 'email', 'password'),
                    success: function() {
                        var credentials = {
                            'identification': self.get('username'),
                            'password': self.get('password')
                        }, authenticator = 'simple-auth-authenticator:jwt';
                        self.get('session').authenticate(authenticator, credentials);
                    }
                });
            } else {
                 // password != confirmpassword
            }
        }
    }
});
