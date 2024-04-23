import express from "express";

const app = express();
const port = 3000;

app.get("/",(req,res) => {
    console.log(req);
    res.send(`<h1>Hello</h1>`);
})

app.get("/about",(req,res) => {
    res.send("<h1>About Me</h1><p>My Name is Vaishnav</p>");
})

app.get("/contact",(req,res) => {
    res.send("<h1>Contact Me</h1><p>vaishnavnishanth3@gmail.com</p>");
})

app.listen(port,() => {
    console.log(`Server is UP & RUNNING on port ${port}!`);
})
