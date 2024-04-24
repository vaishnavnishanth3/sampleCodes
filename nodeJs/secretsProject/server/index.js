
import express from "express";
import { dirname } from "path";
import { fileURLToPath } from "url";
import bodyParser from "body-parser";
import morgan from "morgan";

const app = express();
const port = 3000;

var isUserAuthorized = false;

app.use(bodyParser.urlencoded({extende:true}))

function check(req,res,next) {
    console.log(req.body);
    var newpassword = req.body["password"];
    var password = "ILoveProgramming";

    if (newpassword === password) {
        isUserAuthorized = true;
    } else {
        isUserAuthorized = false;
    }
    next();
}

const __dirname = dirname(fileURLToPath(import.meta.url));
console.log(__dirname);

app.use(check);

app.use(morgan('combined'));

app.get("/",(req,res) => {
    res.sendFile(__dirname+"/../public/index.html");
})

app.post("/check",(req,res) => {
    if (isUserAuthorized) {
        
        res.sendFile(__dirname+"/../public/secret.html");
    } else {
        res.sendFile(__dirname+"/../public/index.html");
    }
})

app.listen(port, () => {
    console.log(`Server up and running on port ${port}!`)
})
