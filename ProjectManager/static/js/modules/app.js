/**
 * Created by KEZIAH on 8/27/2015.
 */
define(['knockout'],function(ko){

    return function(){

        ko.components.register('container', { require : 'js/modules/container'});
        ko.components.register('top_nav_bar', { require : 'js/modules/top_nav_bar'});

    }

});