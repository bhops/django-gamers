import DRFAdapter from './drf';
import ENV from 'ember-gamers/config/environment';

export default DRFAdapter.extend({
    namespace: ENV.APP.API_NAMESPACE,
    host: ENV.APP.API_HOST
});
