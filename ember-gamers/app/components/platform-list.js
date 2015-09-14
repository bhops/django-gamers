import Ember from 'ember';

export default Ember.Component.extend({
    actions: {
        selectPlatform: function(platform){
            console.log('Platform selected:', platform.get('name'));
            this.sendAction('selectedPlatform', platform);
        }
    }
});
