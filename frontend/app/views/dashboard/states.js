/**
 * Created by conamerica15 on 30/07/15.
 */
angular.module('myApp.views.states', ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/states', {
            templateUrl: 'views/dashboard/states.html',
            controller: 'stateController'
        });
    }])

    .factory('StateFactory', ['$http', 'myAppConfiguration', function ($http, myAppConfiguration) {

        return {
            getAll: function () {
                return $http.get(myAppConfiguration.url + myAppConfiguration.port + "/states/");
            }
        };

    }])
    .controller("stateController", function ($scope, StateFactory) {

        $scope.status;
        $scope.states;
        $scope.companyState;
        $scope.userCity;

        getStates();

        function getStates() {
            StateFactory.getAll()
                .then(function (data) {
                    $scope.states = data.data;
                }, function error(response) {
                    scope.error = 'Error registrando el Cliente: ' + response.data;
                });

        }
    });