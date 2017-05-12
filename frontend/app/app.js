'use strict';

/**
 * @ngdoc overview
 * @name myApp
 * @description
 * # yapp
 *
 * Main module of the application.
 */
angular.module('myApp', [
    'ngRoute',
    'blockUI',
    'ui.mask',
    'myApp.views.login',
    'myApp.views.company',
    'myApp.views.customer',
    'myApp.views.dashboard',
    'myApp.views.states'
])
    .config(['$locationProvider', '$routeProvider', function ($locationProvider, $routeProvider) {
        $locationProvider.hashPrefix('!');

        $routeProvider.otherwise({redirectTo: '/login'});
    }])
    .provider('myAppConfiguration', function () {
        // default values
        var values = {
            url: 'http://localhost',
            port: ':8000'
        };
        return {
            set: function (constants) { // 1
                angular.extend(values, constants);
            },
            $get: function () { // 2
                return values;
            }
        };
    })
    .config(function (blockUIConfig) {

        // Change the default overlay message
        blockUIConfig.message = 'Cargando...';

        // Change the default delay to 100ms before the blocking is visible
        blockUIConfig.delay = 100;

    });
