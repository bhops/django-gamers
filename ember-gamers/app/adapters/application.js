import Ember from 'ember';
import DS from 'ember-data';
import ENV from 'ember-gamers/config/environment';

export default DS.JSONAPIAdapter.extend({
    namespace: ENV.APP.API_NAMESPACE,
    host: ENV.APP.API_HOST,
});
