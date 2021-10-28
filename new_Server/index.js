import Express from "express";
import * as path from 'path'
import data from './data.js'
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
const app = Express()
const port = 3000
app.use(Express.static("public"))

app.get('/data/:id', (req, res)=>{
    res.send(req.params.id)
})


app.listen(port, ()=> console.log(`Listening on Port ${port}`))