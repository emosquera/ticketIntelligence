'use strict';

/**
 * @ngdoc function
 * @name yapp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of yapp
 */
angular.module('myApp')

    .factory('LoginFactory', ['$http','myAppConfiguration', function ($http, myAppConfiguration) {

        var dataFactory = {};

        dataFactory.authenticate = function (user) {
            return $http.post(myAppConfiguration.url + myAppConfiguration.port + "/users/authenticate/", user);
        };

        return dataFactory;
    }])

    .controller('LoginCtrl', function ($scope, $log, $location, LoginFactory) {
        $scope.submit = function () {
            if ($scope.user.username != undefined && $scope.user.password != undefined) {
                LoginFactory.authenticate($scope.user)
                    .success(function (data) {
                        $scope.result = data;
                        if ($scope.result.status == "SUCCESS") {
                            $location.path('/dashboard');
                            $scope.error = ""
                        } else {
                            $scope.error = $scope.result.msg_status;
                        }
                    })
                    .error(function (error) {
                        $log.debug(error.message);
                        $scope.status = 'No se puede iniciar sesion: ' + error.message;
                    });
                ;
            }
        }
    });
