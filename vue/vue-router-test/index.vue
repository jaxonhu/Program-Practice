<!DOCTYPE html>
<html>
<head>
</head>
<body>
<div id="app">
    <h1> hello world </h1>
    <p>
        <router-link to="/foo">Go To Foo</router-link>
        <router-link to="/bar">Go To bar</router-link>
    </p>
    <router-view></router-view>
</div>

</body>
</html>

<script>
    const Foo = { template: '<div>foo</div>'}
    const Bar = {template: '<div>Bar</div>'}

    const routes = [
        {path: '/foo', component: Foo},
        {path: '/bar', component: Bar}
    ]

    const router = new VueRouter({
        routes
    })

    const app = new Vue({
        router
    }).$mount('#app')
</script>



