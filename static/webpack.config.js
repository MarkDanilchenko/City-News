const path = require('path');
const Dotenv = require('dotenv-webpack');

module.exports = {
	entry: {
		index: path.resolve(__dirname, 'src/js/index.js'),
	},
	output: {
		path: path.resolve(__dirname, 'dist'),
		filename: 'bundle.js',
	},
	mode: 'production',
	module: {
		rules: [
			{ test: /\.css$/, exclude: /node_modules/, use: ['style-loader', 'css-loader'] },
			{ test: /\.js$/, exclude: /node_modules/, use: 'babel-loader' },
		],
	},
    plugins: [
        new Dotenv()
    ]
};
