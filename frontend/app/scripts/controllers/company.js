/**
 * Created by conamerica15 on 31/07/15.
 */
angular.module('myApp')

    .factory('CompanyFactory', ['$http','myAppConfiguration', function ($http, myAppConfiguration) {

        var dataFactory = {};

        dataFactory.save = function (newCompany) {
            return $http.post(myAppConfiguration.url + myAppConfiguration.port +"/companies/", newCompany);
        };

        return dataFactory;
    }])


    .controller("companyController", function ($scope, $log, $location, CompanyFactory) {

        $scope.companyState = new Object();
        $scope.newCompany = new Object();
        $scope.newCompany.user = {};
        $scope.newCompany.address = "";
        $scope.newCompany.phone = "";

        $scope.submit = function () {
            $scope.newCompany.type = 'Company';
            $scope.newCompany.user.id = null;
            $scope.newCompany.user.email = $scope.newCompany.user.email;
            $scope.newCompany.user.username = $scope.newCompany.user.email;
            $scope.newCompany.lastName = "";
            CompanyFactory.save($scope.newCompany)
                .success(function (data) {
                    $scope.result = data;
                    if ($scope.result.status == "SUCCESS") {
                        $location.path('/welcome');
                        $scope.status = 'Establecimiento Registrado';
                        $scope.companyState = new Object();
                        $scope.newCompany = new Object();
                    } else {
                        $scope.errors = $scope.result.msg_status;
                    }
                }).
                error(function (error) {
                    $scope.error = 'Error registrando el Establecimiento: ' + error.message;
                });
        };
    });
