/**
 * Created by conamerica15 on 31/07/15.
 */
angular.module('myApp')

    .factory('UserFactory', ['$http','myAppConfiguration', function ($http, myAppConfiguration) {

        var dataFactory = {};

        dataFactory.save = function (newUser) {
            return $http.post(myAppConfiguration.url + myAppConfiguration.port +"/customers/", newUser);
        };

        return dataFactory;
    }])


    .controller("customerController", function ($scope, $log, $location, UserFactory) {

        $scope.userState = new Object();
        $scope.newUser = new Object();
        $scope.newUser.user = {};
        $scope.newUser.address = "";
        $scope.newUser.homePhone = "";
        $scope.newUser.cellPhone = "";

        $scope.submit = function () {
            $scope.newUser.type = 'Customer';
            $scope.newUser.user.id = null;
            $scope.newUser.user.email = $scope.newUser.email;
            $scope.newUser.user.username = $scope.newUser.email;
            UserFactory.save($scope.newUser)
                .success(function (data) {
                    $scope.result = data;
                    if ($scope.result.status == "SUCCESS") {
                        $location.path('/welcome');
                        $scope.status = 'Usuario Registrado';
                        $scope.userState = new Object();
                        $scope.newUser = new Object();
                    } else {
                        $scope.errors = $scope.result.msg_status;
                    }
                }).
                error(function (error) {
                    $scope.error = 'Error registrando el Usuario: ' + error.message;
                });
        };
    });
