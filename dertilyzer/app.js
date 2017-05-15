/**
 * Copyright 2014-2016 IBM Corp. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

'use strict';

var http = require('http');
var fs = require('fs');
var bodyParser = require("body-parser");
var express = require('express'),
    tradeoffAnalyticsConfig = require('./tradeoff-analytics-config');

var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use('/',express.static(__dirname + '/public'));

app.get('/trade', function(req,res) {
	  res.sendfile(__dirname + '/public/index.html');
	});

app.get('/main', function(req,res) {
	  res.sendfile(__dirname + '/public/demo.html');
	});

	app.post('/login', function(req, res) {
		var state = req.body.inputUsername;
		var county = req.body.inputPassword;
		console.log('req params', state, county);
		var url = "http://cmpe272-python.mybluemix.net/api/crops/" + state + "/" + county;
		http.get(url, function(res) {
		  var body = '';
		  res.on('data', function(data){
			  body += data;
		  	})
		res.on('end', function(){
	        var response = JSON.parse(body);
			fs.writeFile('./public/data.json', response.results, function (err) {});
			})
		  });
		  res.redirect('/trade');
	});
	
	app.post('/login2', function(req, res) {
		fs.readFile('./public/data.json', function (err, data) {
			var body = '';
			req.on('data', function(data){
				  body += data;
			  	})
			 req.on('end', function(){
				 res.setHeader("Content-Type", "text/json");
				 res.setHeader("Access-Control-Allow-Origin", "*");
				 res.end(data.toString());
			  	})
		});
	});

// For local development, copy your service instance credentials here, otherwise you may ommit this parameter
var serviceCredentials = {
  username: 'bec9820d-4d36-4289-98bd-fc0f67dab9d4',
  password: 'oMt3YNT3SyLB'
}
// When running on Bluemix, serviceCredentials will be overriden by the credentials obtained from VCAP_SERVICES
tradeoffAnalyticsConfig.setupToken(app, serviceCredentials); 

// to communicate with the service using a proxy rather then a token, add a dependency on "body-parser": "^1.15.0" 
// to package.json, and use:
// tradeoffAnalyticsConfig.setupProxy(app, serviceCredentials);

var port = process.env.VCAP_APP_PORT || 2000;
app.listen(port);
console.log('listening at:', port);
