new Vue({
    el: '#app',
    delimiters: ['${','}'],
    data: {
        loading: false,
        count_pages: 1,
        current_page: 1,
        next_page: null,
        previous_page: null,
        articles: [],
        tags: [],
    },
    mounted: function() {
        this.getCurrentArticles();
    },
    methods: {
        getCurrentArticles: function() {
            this.getArticlesByPage(this.current_page);
        },
        getArticlesByPage: function(page) {
            this._getArticleTags();
            this.loading = true;
            this.$http.get('/api/post/?page=' + page)
            .then((response) => {
                this.loading = false;
                this.current_page = page;
                this.count_pages = response.data['count_pages'];
                this.next_page = response.data['next_page'];
                this.previous_page = response.data['previous_page'];
                this.articles = response.data['results'];
            })
            .catch((err) => {
                this.loading = false;
                console.log(err);
            })
        },
        _getArticleTags: function() {
            this.loading = true;
            this.$http.get('/api/post/tags/')
            .then((response) => {
                this.loading = false;
                this.tags = response.data;
            })
            .catch((err) => {
                this.loading = false;
                console.log(err);
            })
        },
    }
});
