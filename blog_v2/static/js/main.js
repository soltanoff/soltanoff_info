new Vue({
    el: '#app',
    delimiters: ['${','}'],
    data: {
        loading: false,
        articles: [],
    },
    mounted: function() {
        this.getArticles();
    },
    methods: {
        getArticles: function() {
            this.loading = true;
            this.$http.get('/api/post/')
            .then((response) => {
                this.loading = false;
                this.articles = response.data;
            })
            .catch((err) => {
                this.loading = false;
                console.log(err);
            })
        },
    }
});
