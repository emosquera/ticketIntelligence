/**
 * Created by conamerica15 on 30/07/15.
 */
angular.module('myApp')

    .factory('StateFactory', ['$http', 'myAppConfiguration', function ($http, myAppConfiguration) {

        var dataFactory = {};

        dataFactory.getAll = function () {
            return $http.get(myAppConfiguration.url + myAppConfiguration.port +"/states/");
        };

        return dataFactory;
    }])
    .controller("stateController", function ($scope, StateFactory) {

        $scope.status;
        $scope.states;
        $scope.companyState;
        $scope.userCity;

        getStates();

        function getStates() {
            StateFactory.getAll()
                .success(function (data) {
                    $scope.states = data;
                })
                .error(function (error) {
                    $scope.status = 'Unable to load states data: ' + error.message;
                });
        }
    });