var fib = function(n) {
    var cache = [0, 1];
    var fibInner = function(n) {
        if (cache[n]!==undefined){
         cache[n]=cache[n];   
        }else{
        cache[n] = fibInner(n-1) + fibInner(n-2);
        }
        return cache[n];
    }
    alert(fibInner(n));
    return fibInner;
}(7);
