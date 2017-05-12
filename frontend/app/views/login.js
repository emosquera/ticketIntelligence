'use strict';

/**
 * @ngdoc function
 * @name yapp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of yapp
 */
angular.module('myApp.views.login', ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/login', {
            templateUrl: 'views/login.html',
            controller: 'LoginCtrl'
        });
    }])

    .factory('LoginFactory', ['$http', 'myAppConfiguration', function ($http, myAppConfiguration) {

        return {
            authenticate: function (user) {
                return $http.post(myAppConfiguration.url + myAppConfiguration.port + "/users/authenticate/", user);
            }
        };

    }])

    .controller('LoginCtrl', function ($scope, $log, $location, LoginFactory) {
        $scope.submit = function () {
            if ($scope.user.username != undefined && $scope.user.password != undefined) {
                LoginFactory.authenticate($scope.user)
                    .then(function (data) {
                        $scope.result = data.data;
                        if ($scope.result.status == "SUCCESS") {
                            $location.path('/dashboard');
                            $scope.error = ""
                        } else {
                            $scope.error = $scope.result.msg_status;
                        }
                    }, function error(response) {
                        $scope.status = 'No se puede iniciar sesion: ' + response.data.msg_status;
                    });
                ;
            }
        }
    });
