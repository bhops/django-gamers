import Ember from 'ember';

export default Ember.Controller.extend({
    loginFailed: false,
    isProcessing: false,

    actions: {
        authenticate: function() {
            this.setProperties({ loginFailed: false, isProcessing: true });
            var credentials = this.getProperties('identification', 'password'),
            authenticator = 'simple-auth-authenticator:jwt';
            var self = this;
            this.get('session').authenticate(authenticator, credentials).then(null, function(){
                self.setProperties({ loginFailed: true, isProcessing: false  });
            });
        }
    }
});
