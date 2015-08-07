/**
 * Created by conamerica15 on 31/07/15.
 */
angular.module('myApp')

    .factory('UserFactory', ['$http','myAppConfiguration', function ($http, myAppConfiguration) {

        var dataFactory = {};

        dataFactory.save = function (newUser) {
            return $http.post(myAppConfiguration.url + myAppConfiguration.port +"/customers/", newCompany);
        };

        return dataFactory;
    }])


    .controller("customerController", function ($scope, $log, $location, UserFactory) {

        $scope.companyState = new Object();
        $scope.newCompany = new Object();
        $scope.newCompany.user = {};
        $scope.newCompany.address = "";
        $scope.newCompany.homePhone = "";
        $scope.newCompany.cellPhone = "";

        $scope.submit = function () {
            $scope.newCompany.type = 'Customer';
            $scope.newCompany.user.id = null;
            $scope.newCompany.user.email = $scope.newCompany.email;
            $scope.newCompany.user.username = $scope.newCompany.email;
            UserFactory.save($scope.newCompany)
                .success(function (data) {
                    $scope.result = data;
                    if ($scope.result.status == "SUCCESS") {
                        $location.path('/welcome');
                        $scope.status = 'Usuario Registrado';
                        $scope.companyState = new Object();
                        $scope.newCompany = new Object();
                    } else {
                        $scope.errors = $scope.result.msg_status;
                    }
                }).
                error(function (error) {
                    $scope.error = 'Error registrando el Usuario: ' + error.message;
                });
        };
    });
