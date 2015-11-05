/**
 * Created by KEZIAH on 8/31/2015.
 */
define(['knockout', 'text!templates/container/navigation.html', 'knockout-postbox'],function(ko, htmlString, postbox){

    function viewModel(params){
        var self = this;

        self.clickedContacts = function(){
            ko.postbox.publish("activePage", ['contacts', null, 'Contacts Page'])
        }

        self.clickedTasks = function(){
            ko.postbox.publish("activePage", ['tasks', null, 'Tasks Page'])
        }

        self.clickedIndex = function(){
            ko.postbox.publish("activePage", ['index', null, 'Index Page'])
        }

    }

    return { viewModel: viewModel, template: htmlString };

});
