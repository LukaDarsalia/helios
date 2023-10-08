const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");
const encrypt = require("mongoose-encryption");
const passport = require("passport");
const passportLocalMongoose = require("passport-local-mongoose");
const port = process.env.PORT || 3000;
const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));

const userSchema = new mongoose.Schema({
	username: String,
	posts: Array,
    description: String,
    contr_posts: Array,
    skills: Array,
    embeddings: Array,
    contact_info: String
});

const postSchema = new mongoose.Schema({
	title: String,
    description: String,
	embeddings: Array,
    skills: Array,
    contact_info: String
});

userSchema.plugin(passportLocalMongoose, { usernameField: "username" });

const User = new mongoose.model("User", userSchema);
const Post = mongoose.model("Post", postSchema);


app.get("/", (req, res) => {
    res.render('homepage');
});

app.get('/search', (req, res) => {
    let query = req.body.query;

    res.render('homepage');
});

app.listen(port, function () {
	console.log("Server has started successfully.");
});


