var myApp = angular.module('myApp', []);

myApp.controller('myController', function myController($scope) {
    $scope.messages = [];
    console.log("Foo");
    console.log('Adding listener.');
    var source = new EventSource('/topic/test');
    source.addEventListener('message', function(e){
        console.log('Message');
        console.log(e.data);
        $scope.$apply(function() {
            $scope.messages.push(e.data);
        });
    });
    console.log('Added listener.');
});
