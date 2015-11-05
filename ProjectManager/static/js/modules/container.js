/**
 * Created by KEZIAH on 8/27/2015.
 */
define(['knockout', 'text!templates/container.html', 'knockout-postbox'],function(ko, htmlString, postbox){

    function viewModel(params){
        var self = this;

        ko.components.register('navigation', { require : 'js/modules/container/navigation'});
        ko.components.register('index', { require : 'js/modules/container/index'});
        ko.components.register('contacts', { require : 'js/modules/container/contacts'});
        ko.components.register('tasks', { require : 'js/modules/container/tasks'});

        self.currentPage = ko.observable('index');

        postbox.subscribe("activePage", function(newValue){

            console.log(newValue[0]);

            self.currentPage(newValue[0]);
        });

    }

    return { viewModel: viewModel, template: htmlString };

});