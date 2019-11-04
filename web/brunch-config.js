exports.files = {
    stylesheets: {joinTo: 'app.css'}
};

exports.plugins = {
    postcss: {processors: [require('autoprefixer')]}
};
