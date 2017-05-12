/**
 * Created by conamerica15 on 30/07/15.
 */
angular.module('myApp.cities', ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/cities', {
            templateUrl: 'cities.html',
            controller: 'cityController'
        });
    }])
    .controller("cityController", function ($scope, $http) {

        $http.get("http://localhost:8000/cities/").success(function (data) {
            $scope.cities = data;
        })
    })