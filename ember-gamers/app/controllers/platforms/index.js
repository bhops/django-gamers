import Ember from 'ember';

export default Ember.ArrayController.extend({
    selectedPlatform: null,
    actions: {
        selectPlatform: function(platform) {
            this.setProperties({
                selectedPlatform: platform
            });
            console.log("received action.");
        }
    }
});
