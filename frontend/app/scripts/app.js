'use strict';

/**
 * @ngdoc overview
 * @name myApp
 * @description
 * # yapp
 *
 * Main module of the application.
 */
angular
    .module('myApp', [
        'ui.router',
        'ngAnimate',
        'blockUI',
        'ui.mask'
    ])
    .provider('myAppConfiguration', function () {
        // default values
        var values = {
            url: 'http://192.168.1.109',
            port : ':8000'
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

    })
    .config(function ($stateProvider, $urlRouterProvider) {

        $urlRouterProvider.when('/dashboard', '/dashboard/overview');
        $urlRouterProvider.otherwise('/login');

        $stateProvider
            .state('base', {
                abstract: true,
                url: '',
                templateUrl: 'views/base.html'
            })
            .state('login', {
                url: '/login',
                parent: 'base',
                templateUrl: 'views/login.html',
                controller: 'LoginCtrl'
            })
            .state('dashboard', {
                url: '/dashboard',
                parent: 'base',
                templateUrl: 'views/dashboard.html',
                controller: 'DashboardCtrl'
            })
            .state('overview', {
                url: '/overview',
                parent: 'dashboard',
                templateUrl: 'views/dashboard/overview.html'
            })
            .state('reports', {
                url: '/reports',
                parent: 'dashboard',
                templateUrl: 'views/dashboard/reports.html'
            })
            .state('customer', {
                url: '/customer',
                parent: 'base',
                templateUrl: 'views/customer/customer.html',
                controller: 'customerController'
            })
            .state('company', {
                url: '/company',
                parent: 'base',
                templateUrl: 'views/company/company.html',
                controller: 'companyController'
            })
            .state('welcome', {
                url: '/welcome',
                parent: 'base',
                templateUrl: 'views/welcome/welcome.html'
            })
            .state('states', {
                url: '/states',
                parent: 'dashboard',
                templateUrl: 'views/dashboard/states.html'
            });

    });
